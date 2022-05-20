from flask import render_template,request,redirect,url_for,abort,flash
from . import main
import requests
from .forms import PostForm,CommentForm
from ..models import Post,Comment
from .. import db

from flask_login import login_required,current_user

@main.route('/')
def index():
    quotes=requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    get_quotes=quotes.json()

    return render_template('main/index.html',get_quotes=get_quotes)


@main.route('/quotes',methods=['GET','POST'])
def json_url():
    return render_template('main/quotes.html')


@main.route('/posts',methods=['GET','POST'])
@login_required
def posts():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,content=form.content.data,
                user_id=current_user.id)

        db.session.add(post)
        db.session.commit()

        flash('Thanks for your post!')
        return redirect(url_for('main.blog'))
    return render_template('main/posts.html',title = 'post',form = form)
    
    
@main.route('/blog',methods=['GET','POST'])
def blog():
    posts=Post.query.all()
    comment=Comment.query.all()
    return render_template('main/blog.html',user=current_user,posts=posts,comment=comment) 


@main.route('/comment/<int:user_id>/<int:post_id>',methods=['POST'])
def comment(user_id,post_id):
    form = CommentForm()
    comment_form=comment_form
    if form.validate_on_submit():
        comment = Comment(content=form.content.data,user_id=user_id,post_id=post_id)

        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('main.blog'))
