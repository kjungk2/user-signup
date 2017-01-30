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

def buildForm(name_error,pass_error):
    content = """
    <form class="form" action="/welcome" method="post">
        <label>
            Username <input type="text" name="username"/>
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
        </br>

        <label>
            E-mail <input type="text" name="email"/>
        </label>
        </br>

        <input type="submit" value="Submit"/>
    </form>"""
    return content

class Index(webapp2.RequestHandler):
    def get(self):
        name_error = self.request.get("name_error")
        pass_error = self.request.get("pass_error")

        main_content = buildForm(name_error, pass_error)
        self.response.write(page_header + main_content + page_footer)

class Welcome(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")

        if username == "":
            self.redirect("/?name_error=Provide a valid username")
        if password == "":
            pass
            #self.redirect("/?pass_error=Provide a password")
        else:
            main_content = "<h1>Welcome, {}!</h1>".format(username)
            self.response.write(main_content)

#TODO How do i make a handler to start at /signup?
app = webapp2.WSGIApplication([
    ('/', Index),
    ('/welcome', Welcome)
], debug=True)
