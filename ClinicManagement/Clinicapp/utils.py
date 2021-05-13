import hashlib
from Clinicapp.models import User, Role, Patient, PhieuKham, Diseases, ChiTietDonThuoc, DonThuoc, Medicine, HoaDon
from Clinicapp import db


def read_patient(kw=None, gender=None, date_of_birth=None, ngaykham=None):
    patient = Patient.query

    if kw:
        patient = patient.filter(Patient.name.contains(kw))

    if gender:
        patient = patient.filter(Patient.gender == gender)

    if date_of_birth:
        patient = patient.filter(Patient.date_of_birth == date_of_birth)

    if ngaykham:
        patient = patient.filter(Patient.ngaykham == ngaykham)

    return patient.all()


def check_login(username, password, role=Role.admin):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    user = User.query.filter(User.username == username,
                             User.password == password,
                             User.role == role.admin).first()

    return user


def get_patient_by_id(patient_id):
    return Patient.query.get(patient_id)


def get_phieukham_by_patient_id(patient_id):
    return PhieuKham.query.get(patient_id)


def get_donthuoc_by_patient_id(patient_id):
    return DonThuoc.query.get(patient_id)


def get_benh_by_patient_id(patient_id):
    return Diseases.query.get(patient_id)


def get_user_by_id(user_id):
    return User.query.get(user_id)


#def hoadon_stats(phieukham):
    #tong_tien, tien_kham, tien_thuoc = 0, 0, 0
    #tien_kham = phieukham["tienkham"]
    #for donthuoc in phieukham.don_thuoc.values():
        #tien_thuoc = donthuoc["medicine_amount"] * donthuoc["soluong"]
    #tong_tien = tong_tien + tien_kham + tien_thuoc

    #return tong_tien, tien_thuoc, tien_kham


#def add_hoadon(phieukham):


def register_user(name, email, username, password, avatar):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=name,
             email=email,
             username=username,
             password=password,
             avatar=avatar,
             role=Role.user)
    try:
        db.session.add(u)
        db.session.commit()
        return True
    except:
        return False



