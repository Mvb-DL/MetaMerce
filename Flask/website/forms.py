from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length


#login form class
class LoginForm(FlaskForm):
    email = StringField("Please enter your Email", validators=[Email()])
    password = PasswordField("Enter your Password", validators=[DataRequired()])
    submit = SubmitField("Login")


#signup form class
class SignUpForm(FlaskForm):
    email = EmailField("Your Email", validators=[DataRequired(), Email()])
    user_name = StringField("Which Username?", validators=[DataRequired()])
    first_name = StringField("Your Firstname", validators=[DataRequired()])
    last_name = StringField("Lastname", validators=[DataRequired()])
    password_one = PasswordField("Enter Password", validators=[DataRequired()])
    password_two = PasswordField("Repeat Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")


#update user form
class UpdateForm(FlaskForm):
    first_name = StringField("New Firstname", validators=[Length(min=1, max=30)])
    last_name = StringField("New Lastname", validators=[Length(min=1, max=30)])
    user_name = StringField("New Username", validators=[Length(min=1, max=30)])
    email = EmailField("New Email", validators=[Email()])
    password = PasswordField('New Password', validators=[Length(min=1, max=30)])
    submit = SubmitField("Change Account")


#update company form
class UpdateCompany(FlaskForm):
    company_name = StringField("Enter your new Company name", validators=[Length(min=1, max=30)])
    company_type = StringField("Enter new Company type", validators=[Length(min=1, max=30)])
    company_website_name = StringField("Enter your company website name", validators=[Length(min=1, max=30)])
    company_url = StringField("Please enter the company website url", validators=[Length(min=1, max=30)])
    company_selling_category = StringField("What do your company sell?", validators=[Length(min=1, max=30)])
    submit = SubmitField("Update Company")


#signup company form
class SignUpCompany(FlaskForm):
    company_name = StringField("Enter your Company name", validators=[Length(min=1, max=30)])
    company_type = StringField("What type is your company?", validators=[Length(min=1, max=30)])
    company_website_name = StringField("Enter your company website name", validators=[Length(min=1, max=30)])
    company_url = StringField("Please enter the company website url", validators=[Length(min=1, max=30)])
    company_selling_category = StringField("What do your company sell?", validators=[Length(min=1, max=30)])
    submit = SubmitField("Sign Company")


#Sig Up APU profile
class SignUpAPI(FlaskForm):
    wordpress_username = StringField("Please enter your WordPress Username", validators=[Length(min=1, max=30), DataRequired()])
    application_password = PasswordField('Enter the application password', validators=[DataRequired()])
    application_domain = StringField("Enter the application domain", validators=[DataRequired()])
    submit = SubmitField("Sign up API Profile")