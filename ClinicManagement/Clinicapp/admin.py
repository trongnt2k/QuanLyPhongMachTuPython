from Clinicapp import admin, db
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from Clinicapp.models import Diseases, Medicine, User, Patient, PhieuKham, PhiKham, DonViThuoc, DonThuoc, ChiTietDonThuoc
from flask_login import current_user, logout_user
from flask import redirect


class DonThuocModelView(ModelView):
    can_view_details = True
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated


class DonViThuocModelView(ModelView):
    form_columns = ('donvi', )
    def is_accessible(self):
        return current_user.is_authenticated


class ChiTietDonThuocModelView(ModelView):
    can_view_details = True
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated


class PhieuKhamModelView(ModelView):
    can_view_details = True
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated


class PhiKhamModelView(ModelView):
    form_columns = ('tienkham', )

    def is_accessible(self):
        return current_user.is_authenticated


class DiseasesModelView(ModelView):
    form_columns = ('name', )

    def is_accessible(self):
        return current_user.is_authenticated


class PatientModelView(ModelView):
    can_view_details = True
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated


class MedicineModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated


class UserModelView(ModelView):
    can_view_details = True
    can_export = True

    def is_accessible(self):
        return current_user.is_authenticated


class ContactView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/about-us.html')

    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()

        return redirect("/admin")

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(DiseasesModelView(Diseases, db.session))
admin.add_view(DonViThuocModelView(DonViThuoc, db.session))
admin.add_view(MedicineModelView(Medicine, db.session))
admin.add_view(PhiKhamModelView(PhiKham, db.session))
admin.add_view(PatientModelView(Patient, db.session))
admin.add_view(PhieuKhamModelView(PhieuKham, db.session))
admin.add_view(DonThuocModelView(DonThuoc, db.session))
admin.add_view(ChiTietDonThuocModelView(ChiTietDonThuoc, db.session))
admin.add_view(UserModelView(User, db.session))
admin.add_view(ContactView(name='About Us'))
admin.add_view(LogoutView(name="Logout"))
