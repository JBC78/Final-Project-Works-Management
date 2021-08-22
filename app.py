from flask import Flask
# create an server (app) using the Flask libabry
app = Flask(__name__)
# creat routes(end points) for the server
@app.route("/") # in our app, create a new route, called / 
#what will this route do
def home_page():
    print("Server received request for 'home page'...")
    return "Welcome to my home page"
# about end point
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

# start the server
if __name__ == "__main__":
    app.run(debug=True)