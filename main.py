#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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
    <h1>Signup</h1>
"""

page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    def get(self):

        # username form
        main_content = """
        <form class='form'>
            <label>
                Username <input type="text" name="username"/>
            </label>
            </br>
            <label>
                Password <input type="text" name="password"/>
            </label>
            </br>
            <label>
                Password Verification <input type="text" name="password_verification"/>
            </label>
            </br>
            <label>
                E-mail <input type="text" name="email"/>
            </label>
        </form>
        """



        self.response.write(page_header + main_content + page_footer)

#TODO How do i make a handler to start at /signup?
app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
