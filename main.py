import webapp2
'''
Make a signup page that validates a user's input.
If user submits something invalid, it should print an error message
If it is valid it should redirect to a welcome page
'''

page_header = """
<!DOCTYPE html>
<head>
    <title>Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
        input {
            margin: 2px
        }
    </style>
</head>
<body>
    <h1><a href="/">Signup</a></h1>
"""

page_footer = """
</body>
</html>
"""
import re
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    return username and USER_RE.match(username)

def valid_password(password):
    return password and PASSWORD_RE.match(password)

def valid_email(email):
    if email != "":
        return EMAIL_RE.match(email)
    return True

def buildForm(username,email,name_error,pass_error,verify_error,email_error):
    content = """
    <form class="form" method="post">
        <label>
            Username <input type="text" name="username" value='""" + username + """'/>
        </label>
        <span class='error'>""" + name_error + """</span>
        </br>

        <label>
            Password <input type="password" name="password"/>
        </label>
        <span class='error'>""" + pass_error + """</span>
        </br>

        <label>
            Password Verification <input type="password" name="verify"/>
        </label>
        <span class='error'>""" + verify_error + """</span>
        </br>

        <label>
            E-mail (optional) <input type="text" name="email" value='""" + email + """'/>
        </label>
        <span class='error'>""" + email_error + """</span>
        </br>

        <input type="submit" value="Submit"/>
    </form>"""
    return content

class Index(webapp2.RequestHandler):
    def get(self):
        main_content = buildForm("","","","","","")
        self.response.write(page_header + main_content + page_footer)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        user_error = ""
        pass_error = ""
        verify_error = ""
        email_error = ""
        error_exists = False

        if not valid_username(username):
            error_exists = True
            user_error = "Please enter a valid username"
        if not valid_password(password):
            error_exists = True
            pass_error = "Please enter a valid password"
        elif password != verify:
            error_exists = True
            verify_error = "Passwords don't match"
        if not valid_email(email):
            error_exists = True
            email_error = "Please enter a valid e-mail"

        if error_exists:
            main_content = buildForm(username,email,user_error,pass_error,verify_error,email_error)
            self.response.write(page_header + main_content + page_footer)
            #self.redirect("/")

        else:
            self.redirect("/welcome?username=" + username)

class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        main_content = "<h1>Welcome, {}!</h1>".format(username)
        self.response.write(main_content)

#TODO How do i make a handler to start at /signup?
app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome)
], debug=True)
