import os
from flask import render_template, request, redirect
from Clinicapp import app, login, utils, decorator
from Clinicapp.admin import *
from Clinicapp.models import *
from flask_login import login_user


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/register', methods=['get', 'post'])
def register():
    err_msg = ""
    if request.method == 'POST':
        password = request.form.get('password')
        confirm = request.form.get('confirm-password')
        if password == confirm:
            name = request.form.get('name')
            email = request.form.get('email')
            username = request.form.get('username')
            f = request.files["avatar"]
            avatar_path = 'images/upload/%s' % f.filename
            f.save(os.path.join(app.root_path, 'static/', avatar_path))
            if utils.register_user(name=name, username=username, password=password,
                                   email=email, avatar=avatar_path):
                return redirect('/')
            else:
                err_msg = "Hệ thống đang bị lỗi! Vui lòng thực hiện sau!"
        else:
            err_msg = "Mật khâu KHÔNG khớp!"

    return render_template('register.html', err_msg=err_msg)


@app.route("/medical-checklist")
def medical_checklist():
    kw = request.args.get('kw')
    gender = request.args.get('gender')
    date_of_birth = request.args.get('date_of_birth')
    ngaykham = request.args.get('ngaykham')
    patient = utils.read_patient(kw=kw,
                                 gender=gender,
                                 date_of_birth=date_of_birth,
                                 ngaykham=ngaykham)

    return render_template('medical-checklist.html',
                           patient=patient)


@app.route("/phieukham/<int:patient_id>")
def phieukham_detail(patient_id):
    patient = utils.get_patient_by_id(patient_id=patient_id)
    phieukham = utils.get_phieukham_by_patient_id(patient_id=patient_id)
    loaibenh = utils.get_benh_by_patient_id(patient_id=patient_id)
    donthuoc = utils.get_donthuoc_by_patient_id(patient_id=patient_id)
    return render_template('phieukhambenh.html',
                           patient=patient,
                           phieukham=phieukham,
                           loaibenh=loaibenh,
                           donthuoc=donthuoc)


@app.route("/login-admin", methods=["post", "get"])
def login_admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password", "")
        user = utils.check_login(username=username,
                                 password=password)
        if user:
            login_user(user=user)
    return redirect("/admin")


@login.user_loader
def user_load(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)
