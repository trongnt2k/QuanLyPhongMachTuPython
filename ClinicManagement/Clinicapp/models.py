from sqlalchemy import Column, Integer, Float, DATE, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from Clinicapp import db, admin
import enum
from flask_login import UserMixin


class Gender(enum.Enum):
    male = 0
    female = 1
    other = 2

    def __str__(self):
        return self.name


class Role(enum.Enum):
    user = 0
    admin = 1


class DonViThuoc(db.Model):
    __tablename__ = 'donvithuoc'
    id = Column(Integer, primary_key=True, autoincrement=True)
    donvi = Column(String(50), nullable=False)
    thuoc_donvithuoc = relationship('Medicine', backref='donvithuoc', lazy=True)

    def __str__(self):
        return str(self.donvi)


class ClinicBase(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __str__(self):
        return str(self.name)


class User(ClinicBase, UserMixin):
    __tablename__ = "user"

    email = Column(String(100))
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    avatar = Column(String(50))
    active = Column(Boolean, default=True)
    role = Column(db.Enum(Role), default=Role.user)
    phieu_kham = relationship('PhieuKham', backref='user', lazy=True)
    hoadon = relationship('HoaDon', backref='user', lazy=True)


class Patient(ClinicBase):
    __tablename__ = 'patient'

    gender = Column(db.Enum(Gender), nullable=False)
    date_of_birth = Column(DATE())
    address = Column(String(50))
    description = Column(String(100))
    ngaykham = Column(DATE())
    phieu_kham_benh = relationship('PhieuKham', backref='patient', lazy=True)


class Medicine(ClinicBase):
    __tablename__ = 'medicine'

    donvithuoc_id = Column(Integer, ForeignKey(DonViThuoc.id),
                           nullable=False)
    medicine_amount = Column(Integer)
    soluong = Column(Integer)
    chi_tiet_don_thuoc = relationship('ChiTietDonThuoc', backref='medicine', uselist=False, lazy=True)


class Diseases(ClinicBase):
    __tablename__ = 'diseases'
    phieukham_loaibenh = relationship('PhieuKham', backref='diseases', lazy=True)



class PhiKham(db.Model):
    __tablename__ = 'phikham'

    idphikhambenh = Column(Integer, primary_key=True, autoincrement=True)
    tienkham = Column(Integer, nullable=False)
    benh_phieukham = relationship('PhieuKham', backref='phikham', lazy=True)

    def __str__(self):
        return str(self.tienkham)


class PhieuKham(db.Model):
    __tablename__ = 'phieukham'

    idphieukham = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey(Patient.id),
                        nullable=False)
    user_id = Column(Integer, ForeignKey(User.id),
                     nullable=False)
    phikhambenh_id = Column(Integer, ForeignKey(PhiKham.idphikhambenh),
                            nullable=False)
    disease_id = Column(Integer, ForeignKey(Diseases.id))
    trieuchung = Column(String(50))
    description = Column(String(50))
    hoa_don = relationship('HoaDon', backref='phieukham', lazy=True)
    don_thuoc = relationship('DonThuoc', backref='phieukham', lazy=True)


class HoaDon(db.Model):
    __tablename__ = 'hoadon'

    idhoadon = Column(Integer, primary_key=True, autoincrement=True)
    phieukhambenh_id = Column(Integer, ForeignKey(PhieuKham.idphieukham),
                              nullable=False)
    user_id = Column(Integer, ForeignKey(User.id),
                     nullable=False)
    tongtien = Column(Integer)



class DonThuoc(db.Model):
    __tablename__ = 'donthuoc'

    iddonthuoc = Column(Integer, primary_key=True, autoincrement=True)
    phieukham_id = Column(Integer, ForeignKey(PhieuKham.idphieukham),
                          nullable=False)
    chitiet_donthuoc = relationship('ChiTietDonThuoc', backref='donthuoc', uselist=False, lazy=True)


class ChiTietDonThuoc(db.Model):
    __tablename__ = 'chitietdonthuoc'

    donthuoc_id = Column(Integer, ForeignKey(DonThuoc.iddonthuoc), primary_key=True,
                         nullable=False)
    thuoc_id = Column(Integer, ForeignKey(Medicine.id), primary_key=True,
                      nullable=False)
    soluong = Column(Integer)
    cachdung = Column(String(50))


if __name__ == '__main__':
    db.create_all()
