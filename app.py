from flask import Flask
from views import views

app = Flask(__name__)   #initialises the application

app.register_blueprint(views,url_prefix="/")

# @app.route("/")  
# def home():
#     return "this is the home page"

if __name__ == '__main__':  
    app.run(debug=True,port=8000)