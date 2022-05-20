from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo


class PostForm(FlaskForm):
    title=StringField('Enter a title',validators = [DataRequired()])
    username = StringField('Enter your username',validators = [DataRequired()])
    content=TextAreaField('Write your blog',validators = [DataRequired()])
    submit = SubmitField('Publish post')

class CommentForm(FlaskForm):
    content = TextAreaField('comment',validators=[DataRequired()])
    submit = SubmitField('comment')