from typing import Any, Mapping
from django import forms
from django.contrib.auth.models import User
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from . import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Doctor,Admin,Patient,Appointment,PatHealth,PatAdmit,DoctorProfessional,Medicines
import datetime
from django.forms.widgets import SelectDateWidget
from django.utils import timezone

dep=[('General Physiciant','General Physician'),
('Dermatologist','Dermatologist'),
('Emergency Medicine Specialist','Emergency Medicine Specialist'),
('Pediatrician','Pediatrician'),
('Anesthesiologist','Anesthesiologist'),
('Colon and Rectal Surgeon','Colon and Rectal Surgeon'),
]

vaccines = {
    # "BCG": "BCG",
    # "OPV(0)": "OPV(0)",
    # "Hep B": "Hep B",
    "OPV1": "OPV1",
    "Penta1(DPT+HepB+HiB)": "Penta1(DPT+HepB+HiB)",
    "OPV2": "OPV2",
    "Penta2(DPT+HepB+HiB)": "Penta2(DPT+HepB+HiB)",
    "OPV3": "OPV3",
    "Penta3(DPT+HepB+HiB)": "Penta3(DPT+HepB+HiB)",
    "IPV": "IPV",
    "MMR-1": "MMR-1",
    "/MR/Measels": "/MR/Measels",
    "JE Vaccine-1": "JE Vaccine-1",
    "OPV Booster": "OPV Booster",
    "DPT 1st Booster": "DPT 1st Booster",
    "JE Vaccine-2": "JE Vaccine-2",
    "DPT 2nd Booster" : "DPT 2nd Booster",
    "TT1" : "TT1",
    "TT2" : "TT2"
}

villages = [
    ('Arookutty', 'Arookutty'),
    ('Aroor', 'Aroor'),
    ('Cherthala North', 'Cherthala North'),
    ('Cherthala South', 'Cherthala South'),
    ('Ezhupunna', '	Ezhupunna'),
    ('Pallippuram', 'Pallippuram'),
    ('Panavally', 'Panavally'),
    ]

class ContactusForm(forms.Form):    #contact us form (feedback), used by patients/doctors to send feedbacks using mail to admins
    Name = forms.CharField(max_length=30,label="",widget=forms.TextInput(attrs={'placeholder': 'NAME'}))
    Name.widget.attrs.update({'class' : 'app-form-control'})
    Email = forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    Email.widget.attrs.update({'class' : 'app-form-control'})
    Message = forms.CharField(max_length=500,label="",widget=forms.TextInput(attrs={'placeholder': 'MESSAGE'}))
    Message.widget.attrs.update({'class' : 'app-form-control'})

class DoctorRegisterForm(UserCreationForm): #used to register a doctor
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    username.widget.attrs.update({'class' : 'app-form-control'})
    
    email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    email.widget.attrs.update({'class' : 'app-form-control'})
    
    firstname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'DOC ID'}))
    firstname.widget.attrs.update({'class' : 'app-form-control'})
    
    # lastname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'LASTNAME'}))
    # lastname.widget.attrs.update({'class' : 'app-form-control'})
    
    dob = forms.DateField(label="",widget=SelectDateWidget(years=range(1960, 2024)))
    dob.widget.attrs.update({'class' : 'app-form-control-date'})
    
    address = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'ADDRESS'}))
    address.widget.attrs.update({'class' : 'app-form-control'})
    
    city = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'CITY'}))
    city.widget.attrs.update({'class' : 'app-form-control'})
    
    country = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'COUNTRY'}))
    country.widget.attrs.update({'class' : 'app-form-control'})
    
    postalcode = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'PHONE NUMBER'}))
    postalcode.widget.attrs.update({'class' : 'app-form-control'})
    
    # image = forms.ImageField(label="")
    # image.widget.attrs.update({'class' : 'app-form-control'})
    
    department = forms.CharField(label="",widget = forms.Select(choices=dep))
    department.widget.attrs.update({'class' : 'app-form-control'})

    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'postalcode','department', 'dob', 'address', 'city', 'country', 'password1', 'password2']
        #fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
    
    def checkdate(self):    #form date of birth validator
        cleaned_data = self.cleaned_data
        db = cleaned_data.get('dob')
        if db < timezone.now().date():
            return True
        self.add_error('dob', 'Invalid date of birth.')
        return False

class DoctorUpdateForm(forms.ModelForm):    #used to edit a doctor instance
    firstname = forms.CharField()
    lastname = forms.CharField()
    #age = forms.IntegerField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2024)))
    address = forms.CharField() 
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)
    appfees = forms.FloatField()
    admfees = forms.FloatField()
    class Meta:
        model = Doctor
        fields = ['firstname', 'lastname', 'dob', 'address', 'city', 'country', 'postalcode', 'image','appfees','admfees']


class AdminRegisterForm(UserCreationForm):  #used to register an admin
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'HOSPITAL'}))
    username.widget.attrs.update({'class' : 'app-form-control'})
    
    email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    email.widget.attrs.update({'class' : 'app-form-control'})

    # phone_number = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'PHONE'}))
    # phone_number.widget.attrs.update({'class' : 'app-form-control'})
    
    firstname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'HOSPITAL ID'}))
    firstname.widget.attrs.update({'class' : 'app-form-control'})
    
    # lastname = forms.CharField(required=False, label="",widget=forms.TextInput(attrs={'placeholder': 'LASTNAME'}))
    # lastname.widget.attrs.update({'class' : 'app-form-control'})
    
    
    # dob = forms.DateField(required=False, label="",widget=SelectDateWidget(years=range(1960, 2021)))
    # dob.widget.attrs.update({'class' : 'app-form-control-date'})
    
    address = forms.CharField(required=False, label="",widget=forms.TextInput(attrs={'placeholder': 'ADDRESS'}))
    address.widget.attrs.update({'class' : 'app-form-control'})
    
    city = forms.CharField(required=False, label="",widget=forms.TextInput(attrs={'placeholder': 'CITY'}))
    city.widget.attrs.update({'class' : 'app-form-control'})
    
    country = forms.CharField(required=False, label="",widget=forms.TextInput(attrs={'placeholder': 'COUNTRY'}))
    country.widget.attrs.update({'class' : 'app-form-control'})
    
    postalcode = forms.IntegerField(required=False, label="",widget=forms.TextInput(attrs={'placeholder': 'POSTAL CODE'}))
    postalcode.widget.attrs.update({'class' : 'app-form-control'})
    
    # image = forms.ImageField(label="")
    # image.widget.attrs.update({'class' : 'app-form-control'})
    
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname','address','city', 'country', 'postalcode', 'password1', 'password2']
        # fields = ['username', 'email', 'firstname', 'lastname', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2','image']
        help_texts = {k:"" for k in fields}

class AdminUpdateForm(forms.ModelForm): #used to edit an admin instance
    firstname = forms.CharField()
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Admin
        fields = ['firstname', 'address', 'city', 'country', 'postalcode', 'image']


class PatientRegisterForm(UserCreationForm):    #used to register a patient
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    username.widget.attrs.update({'class' : 'app-form-control'})
    
    email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    email.widget.attrs.update({'class' : 'app-form-control'})
    
    firstname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'CHILD ID'}))
    firstname.widget.attrs.update({'class' : 'app-form-control'})
    
    # lastname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'LASTNAME'}))
    # lastname.widget.attrs.update({'class' : 'app-form-control'})
      
    dob = forms.DateField(label="",widget=SelectDateWidget(years=range(1960, 2025)))
    dob.widget.attrs.update({'class' : 'app-form-control-date'})
    
    address = forms.TypedChoiceField(label="", choices=villages)
    address.widget.attrs.update({'class' : 'app-form-control'})
    
    city = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'CITY'}))
    city.widget.attrs.update({'class' : 'app-form-control'})
    
    country = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'COUNTRY'}))
    country.widget.attrs.update({'class' : 'app-form-control'})
    
    postalcode = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'PHONE'}))
    postalcode.widget.attrs.update({'class' : 'app-form-control'})

    height = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'HEIGHT'}))
    height.widget.attrs.update({'class' : 'app-form-control'})

    weight = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'WEIGHT'}))
    weight.widget.attrs.update({'class' : 'app-form-control'})
    

    # image = forms.ImageField(label="")
    # image.widget.attrs.update({'class' : 'app-form-control'})
    
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

    # pin = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'PINCODE'}))
    # pin.widget.attrs.update({'class' : 'app-form-control'})

    class Meta:
        model = User
        # fields = ['username', 'email', 'firstname', 'lastname', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2','image']
        fields = ['username', 'email', 'firstname', 'dob', 'height', 'weight', 'address', 'city', 'country', 'postalcode', 'password1', 'password2']

        help_texts = {k:"" for k in fields}



class WorkerRegisterForm(UserCreationForm):    #used to register a patient
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    username.widget.attrs.update({'class' : 'app-form-control'})
    
    email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    email.widget.attrs.update({'class' : 'app-form-control'})
    
    worker_id = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Worker ID'}))
    worker_id.widget.attrs.update({'class' : 'app-form-control'})
    
    village = forms.TypedChoiceField(label="")
    village.widget.attrs.update({'class' : 'app-form-control'})
    
    phone_number = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'PHONE'}))
    phone_number.widget.attrs.update({'class' : 'app-form-control'})
        
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['village'].choices = [
             ('Arookutty', 'Arookutty'),
             ('Aroor', 'Aroor'),
             ('Cherthala North', 'Cherthala North'),
             ('Cherthala South', 'Cherthala South'),
             ('Ezhupunna', '	Ezhupunna'),
             ('Pallippuram', 'Pallippuram'),
             ('Panavally', 'Panavally'),
        ]
    # ('abc', 'abc'),
    # ('mno', 'mno'),
    class Meta:
        model = User
        # fields = ['username', 'email', 'firstname', 'lastname', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2','image']
        fields = ['username', 'email', 'worker_id', 'village', 'phone_number', 'password1', 'password2']

        help_texts = {k:"" for k in fields}



class PatientUpdateForm(forms.ModelForm):   #used to update a patient
    firstname = forms.CharField()
    lastname = forms.CharField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2024)))
    address = forms.TypedChoiceField(choices=villages)
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Patient
        fields = ['firstname', 'lastname', 'dob', 'address', 'city', 'country', 'postalcode', 'image']


class PatientAppointmentForm(forms.ModelForm):      #used to register an appointment by patient
    doctor = forms.TypedChoiceField(label='')
    doctor.widget.attrs.update({'class' : 'app-form-control'})
    # doctorId=forms.CharField(widget=forms.Select(choices="c"))  
    calldate = forms.DateField(label='',widget=SelectDateWidget(years=range(2021,2025)))    #date of appointment
    calldate.widget.attrs.update({'class' : 'app-form-control-date'})
    calltime = forms.TypedChoiceField(label='') #time of appointment
    calltime.widget.attrs.update({'class' : 'app-form-control'})
    description = forms.TypedChoiceField(label='', choices = vaccines)
    # description.widget.attrs.update({'class' : 'app-form-control'}) 
    
    def __init__(self, *args, **kwargs):
        super(PatientAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].choices = [(c.id, c.firstname+"("+c.department+")") for c in Doctor.objects.filter(status=True).all()]#list of doctors to choose from, taken fresh from database
        self.fields['calltime'].choices = [('9:00','9:00 AM'),('9:15','9:15 AM'),('9:30','9:30 AM'),('9:45','9:45 AM'),('10:00','10:00 AM'),('10:15','10:15 AM'),('10:30','10:30 AM'),('10:45','10:45 AM'),('11:00','11:00 AM'),('11:15','11:15 AM'),('11:30','11:30 AM'),('11:45','11:45 AM'),('12:00','12:00 PM'),('12:15','12:15 PM'),('12:30','12:30 PM'),('12:45','12:45 PM'),
                                            ('14:00','02:00 PM'),('14:15','02:15 PM'),('14:30','02:30 PM'),('14:45','02:45 PM'),('15:00','03:00 PM'),('15:15','03:15 PM'),('15:30','03:30 PM'),('15:45','03:45 PM'),('16:00','04:00 PM'),('16:15','04:15 PM'),('16:30','04:30 PM'),('16:45','04:45 PM'),('17:00','05:00 PM')]
                                            #choices for time slot for appointment
        self.fields['description'].widget.attrs.update({'class' : 'app-form-control', 'placeholder' : 'Vaccines'})
    class Meta:
        model=Appointment
        fields=['description','calldate','calltime']




class AdminAppointmentForm(forms.ModelForm):     #used to register an appointment by admin
    doctor = forms.TypedChoiceField(label='')   #doctor is chosed from existing doctors in hospital database
    doctor.widget.attrs.update({'class' : 'app-form-control'})
    patient = forms.TypedChoiceField(label='')  #patient is chosed from existing doctors in hospital database
    patient.widget.attrs.update({'class' : 'app-form-control'})
    calldate = forms.DateField(label='',widget=SelectDateWidget(years=range(2021,2025)))    #date of appointment
    calldate.widget.attrs.update({'class' : 'app-form-control-date'})
    calltime = forms.TypedChoiceField(label='') #time of appointment
    calltime.widget.attrs.update({'class' : 'app-form-control'})
    description = forms.TypedChoiceField(label='', choices=vaccines)
    description.widget.attrs.update({'class' : 'app-form-control'}) 
    def __init__(self, *args, **kwargs):
        super(AdminAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].choices = [(c.id, c.firstname+"("+c.department+")") for c in Doctor.objects.filter(status=True).all()]#list of doctors to choose from, taken fresh from database
        self.fields['patient'].choices = [(c.id, c.firstname) for c in Patient.objects.filter(status=True).all()]#list of patients to choose from, taken fresh from database
        self.fields['calltime'].choices = [('9:00','9:00 AM'),('9:15','9:15 AM'),('9:30','9:30 AM'),('9:45','9:45 AM'),('10:00','10:00 AM'),('10:15','10:15 AM'),('10:30','10:30 AM'),('10:45','10:45 AM'),('11:00','11:00 AM'),('11:15','11:15 AM'),('11:30','11:30 AM'),('11:45','11:45 AM'),('12:00','12:00 PM'),('12:15','12:15 PM'),('12:30','12:30 PM'),('12:45','12:45 PM'),
                                            ('14:00','02:00 PM'),('14:15','02:15 PM'),('14:30','02:30 PM'),('14:45','02:45 PM'),('15:00','03:00 PM'),('15:15','03:15 PM'),('15:30','03:30 PM'),('15:45','03:45 PM'),('16:00','04:00 PM'),('16:15','04:15 PM'),('16:30','04:30 PM'),('16:45','04:45 PM'),('17:00','05:00 PM')]
                                            #choices for time slot for appointment
    
    class Meta:
        model=Appointment
        fields=['description','calldate','calltime']



class YourHealthEditForm(forms.ModelForm):  #patient can edit their health information
    height = forms.FloatField()
    weight = forms.FloatField()
    age = forms.IntegerField()
    diseases = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 10}))
    medicines = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 10}))
    ts  = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 10}))
    class Meta:
        model = PatHealth
        fields = ['height','weight','diseases','medicines','ts', 'age']
    
        
class AppointmentEditForm(forms.ModelForm): #doctor can edit appointment description field, be it adding new lines or deleting a few of the old one
    description = forms.CharField(max_length=300,label='',widget=forms.TextInput(attrs={'placeholder': 'DESCRIPTION'}))
    description.widget.attrs.update({'class' : 'app-form-control'}) 
    class Meta:
        model = Appointment
        fields = ['description']

class AdmitRegisterForm(forms.ModelForm):   #doctor can admit a patient
    description = forms.CharField(max_length=300,label='',widget=forms.TextInput(attrs={'placeholder': 'DESCRIPTION'}))
    description.widget.attrs.update({'class' : 'app-form-control'}) 
    admitDate = forms.DateField(label='',widget=SelectDateWidget)
    admitDate.widget.attrs.update({'class' : 'app-form-control-date'})
    class Meta:
        model = PatAdmit
        fields = ['description','admitDate']

class AdminAdmitRegisterForm(forms.ModelForm):  #admin can admit a patient
    doctor = forms.TypedChoiceField(label='')   #doctor is chosed from existing doctors in hospital database
    doctor.widget.attrs.update({'class' : 'app-form-control'})
    patient = forms.TypedChoiceField(label='')  #patient is chosed from existing doctors in hospital database
    patient.widget.attrs.update({'class' : 'app-form-control'})
    description = forms.CharField(max_length=300,label='',widget=forms.TextInput(attrs={'placeholder': 'DESCRIPTION'}))
    description.widget.attrs.update({'class' : 'app-form-control'}) 
    admitDate = forms.DateField(label='',widget=SelectDateWidget) 
    admitDate.widget.attrs.update({'class' : 'app-form-control-date'})
    
    def __init__(self, *args, **kwargs):
        super(AdminAdmitRegisterForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].choices = [(c.id, c.firstname+"("+c.department+")") for c in Doctor.objects.filter(status=True).all()]#list of doctors to choose from, taken fresh from database
        self.fields['patient'].choices = [(c.id, c.firstname) for c in Patient.objects.filter(status=True).all()]#list of patients to choose from, taken fresh from database

    class Meta:
        model = PatAdmit
        fields = ['description','admitDate']


class DoctorProfessionalUpdateForm(forms.ModelForm):    #doctor can edit their feees
    appfees = forms.FloatField(label='',widget=forms.TextInput(attrs={'placeholder': 'APPOINTMENT FEES'}))
    appfees.widget.attrs.update({'class' : 'app-form-control'})
    admfees = forms.FloatField(label='',widget=forms.TextInput(attrs={'placeholder': 'ADMIT FEES'}))
    admfees.widget.attrs.update({'class' : 'app-form-control'})
    class Meta:
        model = DoctorProfessional
        fields = ['appfees','admfees']


class AddMedForm(forms.ModelForm):  #admin can add medicines to database
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'NAME'}))
    name.widget.attrs.update({'class' : 'app-form-control'})
    price = forms.FloatField(label='',widget=forms.TextInput(attrs={'placeholder': 'PRICE'}))
    price.widget.attrs.update({'class' : 'app-form-control'})
    class Meta:
        model = Medicines
        fields = ['name','price']

class OpcostsForm(forms.Form):  #admin can change hospital operation charges, like maintenence fee
    maintenance = forms.FloatField(label='',widget=forms.TextInput(attrs={'placeholder':'MAINTAINANCE CHARGE'}))
    maintenance.widget.attrs.update({'class' : 'app-form-control'})
    hospfee = forms.FloatField(label='',widget=forms.TextInput(attrs={'placeholder': 'HOSPITAL FEE'}))
    hospfee.widget.attrs.update({'class' : 'app-form-control'})
    roomfee = forms.FloatField(label='',widget=forms.TextInput(attrs={'placeholder': 'ROOM FEE'}))
    roomfee.widget.attrs.update({'class' : 'app-form-control'})

class CovidVaccinationApplicationForm(forms.Form):  #patient can apply for covid vaccine
    commodity = forms.TypedChoiceField(label='')    #choose type of vaccine
    commodity.widget.attrs.update({'class' : 'app-form-control'})
    
    def __init__(self, *args, **kwargs):
        super(CovidVaccinationApplicationForm, self).__init__(*args, **kwargs)
        covaxin = Medicines.objects.all().filter(name="covaxin").first()    #fetch covaxin vaccine information from database
        covishield = Medicines.objects.all().filter(name="covishield").first()  #fetch covishield vaccine information from database
        self.fields['commodity'].choices = [(covaxin.id, covaxin.name), (covishield.id, covishield.name)]