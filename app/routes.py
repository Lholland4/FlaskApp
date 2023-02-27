from flask import Flask, render_template, flash, redirect, request, url_for, jsonify
from app.forms import LoginForm
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'lholland'}
    classes = [{'classInfo': {'code':'CSC324', 'title': 'DevOps'}, 'instructor': 'Baoqiang Yan'},
    {'classInfo': {'code': 'CSC184', 'title': 'Python Programming'}, 'instructor': 'Evan Noynaert'}]
    return render_template('index.html', title='Home', user=user, classes=classes) 

@app.route('/lholland')
def username():
    return render_template('lholland.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Welcome user {}! You opted for remember_me={}'.format(
                form.username.data, form.remember_me.data))
            return redirect('/lholland')
    else:
        if request.args:
            flash('GET method now allowed for login!')
        # else:
        #     flash('No data in request!')

    return render_template('login.html', title='Sign In', form=form)
@app.route("/restlogin", methods=["GET", "POST"])
def rest_login():
    json_data = request.get_json(force=True)
    if json_data:
        username = json_data["username"]
        password = json_data["password"]
    else:
        return '{"Success":false}'
    if username == "lholland" and password == "123":
        return '{"Success":true}'
    return '{"Success":false}'

@app.route('/json')
def jsonTest():
    # return jsonify(list(range(5)))
    instructor = {"username": "byan",
            "role": "instructor",
            "uid": 11,
            "name":
            {"firstname": "Baoqiang",
                "lastname": "Yan"
                }
            }
    return jsonify(instructor)

{"username":"byan",
"role":"instructor",
"uid":11,
"name":{"firstname":"Baoqiang", "lastname":"Yan"}}

