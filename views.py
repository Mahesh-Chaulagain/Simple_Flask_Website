from flask import Blueprint,render_template,request,jsonify,redirect,url_for

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html",name="ram") #name is the template variables

@views.route("/profile") #<username> is the URL parameter
def profile():
    # args = request.args #access query parameters
    # name = args.get('name')
    # return render_template("index.html",name=name)  #to acces type: http://127.0.0.1:8000/views/profile?name=hari
    return render_template("profile.html")

#Returning json
@views.route("/json")
def get_json():
    return jsonify({
        'name':'ram',
        'age':20
    })

#Getting json data
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

#redirecct
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))