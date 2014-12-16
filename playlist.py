import jinja2
import os
import webapp2
import logging

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())
        
class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('contact.html')
        self.response.out.write(template.render())
        
routes = [
    ('/index.html', HelloHandler),
    ('/contact.html', ContactHandler),
]

app = webapp2.WSGIApplication(routes, debug
