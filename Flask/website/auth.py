from flask import Blueprint, render_template, request, flash, redirect, url_for, session, make_response
from .models import User, SubscriperUser
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .forms import LoginForm, SignUpForm, SignUpCompany, UpdateCompany, SignUpAPI, UpdateForm
from .controllers.user_controller import UserController
from .controllers.company_controller import CompanyController
from .controllers.api_controller import ApiController

UC = UserController()
CC = CompanyController()
AC = ApiController()

auth = Blueprint('auth', __name__)


#function to login the user
@auth.route('/login', methods=["GET", 'POST'])
def login():

    #import login form from forms
    login_form = LoginForm()
    form = SignUpForm()

    if request.method == 'POST' and login_form.validate_on_submit:

            email = login_form.email.data
            password = login_form.password.data

            user = User.query.filter_by(email=email).first()

            if user and user.verify_password(password):

                session["email"] = email
                
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)

                resp = make_response(redirect(url_for('views.home')))
                resp.set_cookie('Usermail', f'{email}')

                return resp

            else:
                #if the user puts in the wrong password he is getting an error message
                flash('Incorrect password, try again.', category='error')
                return render_template("auth/login.html", user=current_user, login_form=login_form, form=form)

    return render_template("auth/login.html", user=current_user, login_form=login_form, form=form)


#get the set cookie
@auth.route('/getcookie')
def getcookie():
    name = request.cookies.get('Usermail')
    return f"The Mail : {name}"


#function to logout the user
@auth.route('/logout')
@login_required
def logout():
    session.pop('email', None)
    logout_user()
    return redirect(url_for('views.landingpage'))


#function for user registration
@auth.route('/sign_up', methods=['POST'])
def sign_up():

    form = SignUpForm()
    login_form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit:

            email = form.email.data
            user_name = form.user_name.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            password_one = form.password_one.data
            password_two = form.password_two.data

            user = User.query.filter_by(email=email).first()

            if user:
                flash('Email already exists.', category='error')
            elif len(email) < 4:
                flash('Email must be greater than 3 characters.', category='error')
            elif len(first_name) < 1:
                flash('First name must be greater than 1 character.', category='error')
            elif len(last_name) < 1:
                flash('Last name must be greater than 1 character.', category='error')
            elif len(user_name) < 1:
                flash('Username must be greater than 1 character.', category='error')
            elif password_one != password_two:
                flash('Passwords do not match.', category='error')
            elif len(password_one) < 7:
                flash('Password must be at least 7 characters.', category='error')

            else:

                new_user = UC.create_user(email, first_name, last_name, user_name, password_one)

                login_user(new_user, remember=True)

                flash('Account created!', category='success')
                return redirect(url_for('views.home'))
    
    return render_template("auth/login.html", user=current_user, form=form, login_form=login_form)


#update User data
@auth.route('/update_account', methods=["GET",'POST'])
def update_account():

    form = UpdateForm(request.form, obj=current_user)

    if request.method == 'POST' and form.validate_on_submit():

        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.user_name = form.user_name.data
        current_user.email = form.email.data

        db.session.commit()
        flash("User was updated", category="success")
        users = User.query.filter(User.id==current_user.id)
        return render_template("account.html", user=current_user, users=users)

    return render_template("auth/update_account.html", form=form, user=current_user)



#there is the functionality given that the user can add his company profile products are connected to the company and a company is connected to a user
@auth.route('/sign_up_company_profile', methods=['GET', 'POST'])
def sign_up_company_profile():

    form = SignUpCompany()

    if request.method == 'POST' and form.validate_on_submit():

        company_name = form.company_name.data
        company_type = form.company_type.data
        company_website_name = form.company_website_name.data
        company_url = form.company_url.data
        company_selling_category = form.company_selling_category.data

        #the company gets saved into the database
        CC.create_company(company_name, company_type, company_website_name, company_url, company_selling_category)
        return redirect(url_for('views.company_profile'))

    return render_template("auth/sign_up_company_profile.html", user=current_user, form=form)


#updates company data
#the user can update his company data and it´s attributes
@auth.route('/update_company_data', methods=['GET', 'POST'])
def update_company_data():

    current_company = CC.get_current_user_company()

    form = UpdateCompany(request.form, obj=current_company)

    if request.method == 'POST' and form.validate_on_submit():

            current_company.company_name = form.company_name.data
            current_company.company_type = form.company_type.data
            current_company.company_website_name = form.company_website_name.data
            current_company.company_url = form.company_url.data
            current_company.company_selling_category = form.company_selling_category.data

            db.session.commit()

            return redirect(url_for('views.company_profile'), code=201)

    return render_template("auth/update_company_data.html", user=current_user, form=form)


#for sign up api profile
@auth.route("/sign_up_api_profile", methods=['GET', 'POST'])
@login_required
def sign_up_api_profile():

    form = SignUpAPI()

    #if the user has no api profile he gets routed to this simple function to create a new account
    if request.method == 'POST' and form.validate_on_submit:

        wordpress_username = form.wordpress_username.data
        application_password = form.application_password.data
        application_domain = form.application_domain.data

        AC.create_api_profile(wordpress_username, application_password, application_domain)

        return redirect(url_for('views.root_API'), code=200)

    return render_template("auth/sign_up_api_profile.html", user=current_user, form=form)



#function that a user can order the newsletter
@auth.route('/new_subscriper', methods=['POST'])
def new_subscriper():

    if request.method == 'POST':

        subscriper_email = request.form.get('subscripe_email')

        subscriper_user = SubscriperUser.query.filter_by(email=subscriper_email).first_or_404()

        if subscriper_user:
            flash('Email already exists.', category='error')

        elif len(subscriper_email) < 4:
            flash('Email must be greater than 3 characters.', category='error')

        else:

            #sends automatically a mail to the new subscriper
            """
            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login('metamerceitc@gmail.com', '12993409')

            msg = MIMEMultipart()
            msg['Subject'] = "Subscriper Mail"
            msg.attach(MIMEText("test"))

            to = [subscriper_email]

            smtpserver.sendmail(from_addr="metamerceitc@gmail.com",
                          to_addrs=to, msg=msg.as_string())
            smtpserver.quit()
            """
            new_subscriper = SubscriperUser(email=subscriper_email)
            db.session.add(new_subscriper)
            db.session.commit()
            flash("Email added! Newsletter is on the way!", category='success')
            return render_template("index.html", user=current_user)
        
    return render_template("index.html", user=current_user)