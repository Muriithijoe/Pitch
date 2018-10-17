from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required,login_user,logout_user
from ..models import Pitch,Comment
from .forms import PitchForm,CommentForm

@main.route('/')
def index():
    title = 'Home'

    pitches = Pitch.get_pitches(id)
    comments=Comment.get_comments(id)

    return render_template('index.html' ,title=title, pitches=pitches,comments=comments)

@main.route('/pitch/new',methods=['GET','POST'])
@login_required
def new_pitch():
    form= PitchForm()
    if form.validate_on_submit():
        title=form.title.data
        description=form.description.data
        new_pitch=Pitch(title=title,description=description)
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title= 'Pitches'
    return render_template('new_pitch.html',pitch_form=form)

@main.route('/comment/new/', methods=['GET','POST'])
@login_required
def new_comment():

    '''
    View new comment route function that returns a page with a form to create a pitch for the specified category
    '''
    comments = Comment.query.all()
    form =CommentForm()
    if form.validate_on_submit():
        name=form.name.data
        new_comment=Comment(name=name)
        new_comment.save_comment()

        return redirect(url_for('.index'))

    title = "New Comment"
    return render_template('new_comment.html', title=title, form=form,comments=comments)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
