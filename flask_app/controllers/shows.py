from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.show import Shows
from flask_app.models.user_login_model import User


@app.route('/new_show')
def new_show():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_show.html',user=User.get_by_id(data))


@app.route('/add_show', methods=['POST'])
def add_show():
    if 'user_id' not in session:
        return redirect('/logout')
        
    data = {
        "show_id": request.form["show_id"],
        "user_id": session["user_id"],
    }
    user_data = {
        "id":session['user_id']
    }
    Shows.favorite(data)
    shows=Shows.get_all_by_user(user_data)

    return render_template('my_shows.html', shows=Shows.get_all_by_user(user_data),user=User.get_by_id(user_data))

@app.route('/edit_show/<int:id>')
def edit_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_show.html",show=Shows.get_one(data),user=User.get_by_id(user_data))

@app.route('/update_show',methods=['POST'])
def update_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Shows.validate_show(request.form):
        return redirect('/new_show')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "id": request.form['id']
    }
    Shows.update(data)
    return redirect('/dashboard')

@app.route('/show_show')
def show_show():
    if 'user_id' not in session:
        return redirect('/logout')
    user_data = {
        "id":session['user_id']
    }
    return render_template("my_shows.html",shows=Shows.get_all_by_user(user_data),user=User.get_by_id(user_data))

@app.route('/one_show/<int:id>')
def one_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("one_show.html",shows=Shows.get_one(data),user=User.get_by_id(user_data))

@app.route('/destroy_show/<int:id>')
def destroy_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Shows.destroy(data)
    return redirect('/dashboard')

@app.route('/')
def shows():
    return render_template("dashboard.html",shows=Shows.get_all())