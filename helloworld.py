import os
import jinja2
import webapp2
import string

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
		
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
	return t.render(params)
	
    def render(self, template, **kw):
	self.write(self.render_str(template, **kw))

class FizzBuzzHandler(Handler):
    

    def get(self):
        n = self.request.get("n")
        n = int(n)
        self.render("fizzbuzz.html",n=n)

class Rot13Handler(Handler):

    def get(self):
        some_text = str(self.request.get("some_text"))
        if some_text:
            
            #some_text = some_text.replace("&gt;", ">")
            #some_text = some_text.replace("&lt;", "<")

            rot13 = string.maketrans( "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
            
            some_text = string.translate(some_text, rot13)
            #some_text = some_text.replace(">", "&gt;")
            #some_text = some_text.replace("<", "&lt;")
        
            self.render("rot13.html", some_text=some_text)
		
		
class MainPage(Handler):
	def get(self):       
                self.render("shopping_list.html", name=self.request.get("name"))
		#output = form_html
		#items = self.request.get_all("food")
		#output_hidden=""
		#if items:
		#    output_items = ""
		#    for item in items:
		#	output_hidden += hidden_html % item
		#	output_items += item_html % item
		
		#    output_shopping = shopping_list_html % output_items
		#    output += output_shopping
		
		#output = output % output_hidden
		
		#self.write(output)
		
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/fizzbuzz', FizzBuzzHandler),
    ('/rot13', Rot13Handler),
], debug=True)
