import datetime
import random
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from .models import *


# Create your views here.
#====================================================================================
def home(request):
    return render(request, 'home.html')
#====================================================================================
def office(request):
    context={
        'appointments' : appointment.objects.count(),
        'doctors' : doctor.objects.count(),
        'patients' : patient.objects.count(),
        'staff':staff.objects.count()
        }
    return render(request, 'office.html', context)
#====================================================================================
def login(request):
    link = 'home'
    if request.method == 'POST':
        user = request.POST['username_input']
        pswd = request.POST['password_input']
        user = authenticate(request=request, username=user, password=pswd)
        if user is not None:
            dj_login(request, user)
            if user.is_superuser:
                link = 'office'
            return redirect(link)
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'login.html') 
#====================================================================================
def logout(request):
    dj_logout(request)
    return redirect('login')
#====================================================================================
def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Successfully created an account for ' + user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'signup.html', context)
#====================================================================================
def forgot(request):
    return render(request, 'forgot.html')
#====================================================================================
def debug(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'empty.html', context)
#====================================================================================
def book(request):
    doc_list = []
    doc = doctor.objects.all()
    for docs in doc:
        doc_list.append(docs)
    
    import datetime
    #dat = datetime.datetime.now().isoformat()
    mindat = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
    date_split = mindat.split('T', maxsplit=1)

    maxdat = (datetime.date.today() + datetime.timedelta(days=30)).isoformat()
    date_split0 = maxdat.split('T', maxsplit=1)

    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        id = request.POST.get('email_id')
        mob_no = request.POST.get('mobile')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        date = datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d')
        doctor_id = request.POST.get('doc')
        temp = doctor.objects.filter(id = doctor_id)
        doctor_name = temp.get(id=doctor_id)
        slot = request.POST.get('slot')
        
        if slot == 'morning':
            lower = 10
            upper = 13
        if slot == 'evening':
            lower = 17
            upper = 19

        temp = time_assign(lower, upper)
        temp2 = time(hour=temp[0], minute=temp[1], second=0, microsecond=0)

        data = appointment(
            fname = first_name,
            lname = last_name,
            email = id,
            mobile = mob_no,
            age = age,
            gender = gender,
            date = date,
            time = temp2,
            doc_id = doctor_id,
            doc_name = doctor_name
        )
        data.save()
        messages.success(request, f'Success! Date : {date.day}-{date.month}-{date.year} at {temp2.hour}:{temp2.minute}')
        return redirect('home')
    return render(request, 'book.html', {
        'doc_list':doc_list,
        'min_date':date_split[0],
        'max_date':date_split0[0]
    })
#====================================================================================
def time_assign(low, up):

    minutes = [15, 30, 45, 0]
    choice = random.randint(0, 1)
    if choice == 0:#time of day = morning
        hrs = random.randint(low, up)
        mins = minutes[random.randint(0, 3)]
        time_temp = [hrs, mins]
    elif choice == 1:#time of day = evening
        hrs = random.randint(low, up)
        mins = minutes[random.randint(0, 3)]
        time_temp = [hrs, mins]

    return time_temp
#====================================================================================
def add_doctor(request):

    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        exp = request.POST.get('exp')
        spec = request.POST.get('spec')
        data = doctor(
            fname = first_name,
            lname = last_name,
            experience = exp,
            speciality = spec
        )

        data.save()
        messages.success(request, f'Success! Doctor {first_name} added to the database')
        return redirect('office')
    return render(request, 'add_doctor.html')
#====================================================================================
def view_patient(request):
    patient_list = []
    patients = patient.objects.all()
    for pat in patients:
        patient_list.append(pat)
    return render(request, 'view_patient.html',{
        'patients':patient_list,
    })
#====================================================================================
def view_appointment(request):
    appointment_list = []
    appoint = appointment.objects.all()
    for app in appoint:
        appointment_list.append(app)
    doc_list = []
    doctor = appointment.objects.all()
    for doctors in doctor:
        doc_list.append(doctors)
    return render(request, 'view_appointment.html',{
        'appointments':appointment_list,
        'doc_list':doc_list
    })
#====================================================================================
def view_doctor(request):
    doctor_list = []
    query = 0
    if request.method == 'POST':
        query = request.POST.get('query')
        doc = doctor.objects.filter(speciality=query)
        for doctors in doc:
            doctor_list.append(doctors)
            return render(request, 'view_doctor.html', {'doctor_list':doctor_list})
    else:
        doc = doctor.objects.all()
        for doctors in doc:
            doctor_list.append(doctors)
        return render(request, 'view_doctor.html', {'doctor_list':doctor_list})
#====================================================================================
def get(request):
    doc_list = []
    doc = doctor.objects.filter(speciality='')
    for docs in doc:
        doc_list.append(docs)
    return render(request, 'book.html', {'doc_list' : doc_list})
#====================================================================================
def open_appointment(request, id):
    data = appointment.objects.filter(id=id)
    data = data.get(id=id)

    if request.method == 'POST':
        decision = request.POST.get('decide')

        if decision == 'Approve':
            doc_id = request.POST.get('id')
            name = request.POST.get('name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            age = request.POST.get('age')
            gender = request.POST.get('gender')

            to_save = patient(
                name = name,
                email = email,
                mobile = mobile,
                age = age,
                gender = gender,
                doc_id = doc_id
            )
            to_save.save()
            data.delete()
            messages.success(request, 'Appoinment approved, now transfered to patients')
            return redirect('office')
        elif decision == 'Disapprove':
            data.delete()
            messages.success(request, 'Appointment disapproved')
            return redirect('office')

    '''
        pid = models.UUIDField(auto_created=True, primary_key=True, unique=True, default=uuid.uuid4, max_length=50)
        fname = models.CharField(max_length=25)
        lname = models.CharField(max_length=25)
        email = models.EmailField()
        mobile = models.CharField(max_length=15)
        age = models.PositiveIntegerField()
        gender = models.CharField(max_length=6)
        doc_id = models.CharField(max_length=50, default='')
    '''
    temp = doctor.objects.filter(id=data.doc_id)
    data.doc_name = temp.get(id=data.doc_id)
    return render(request, 'open_appointment.html', {
        'data':data
    })
#====================================================================================
def patient_details(request, id):
    pat = patient.objects.filter(pid=id)
    pat = pat.get(pid=id)
    temp = doctor.objects.filter(id=pat.doc_id)
    doc = temp.get(id=pat.doc_id)

    if request.method == 'POST':
        discharge = request.POST.get('decide')
        if discharge == 'Discharge':

            id = pat.pid
            name = pat.name
            email = pat.email
            mobile = pat.mobile
            age = pat.age
            gender = pat.gender
            doc_id = doc.id
            doc_name = f"{doc.fname} {doc.lname}"
            doc_spec = doc.speciality

            data = historie(
                pid=id,
                name=name,
                email=email,
                mobile=mobile,
                age=age,
                gender=gender,
                doc_id=doc_id,
                doc_name=doc_name,
                doc_spec=doc_spec,
            )
            data.save()
            pat.delete()
            messages.success(request, 'Patient discharged')
            return redirect('office')

    return render(request, 'patient_details.html', {
        'pat':pat,
        'doc_name':f"{doc.fname} {doc.lname}",
        'doc_spec':doc.speciality
    })
#====================================================================================
def add_staff(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        mobile = request.POST.get('mobile')
        role = request.POST.get('role')

        temp = staff(
            name=name,
            gender=gender,
            age=int(age),
            mobile=mobile,
            role=role
        )
        temp.is_staff = True
        temp.save()
        messages.success(request, 'Staff added')
        return redirect('office')
    return render(request, 'add_staff.html')
#====================================================================================
def remove_staff(request, id):
    temp = staff.objects.filter(sid=id)
    temp = temp.get(sid=id)
    temp.delete()
    messages.success(request, 'Staff removed')
    return redirect('view_staff')
#====================================================================================
def view_staff(request):
    data = staff.objects.all()
    return render(request, 'view_staff.html', {
        "staff":data
    })
#====================================================================================
def prev_appointments(request, id):
    data_list = []
    data = historie.objects.filter(email=id)
    
    for d in data:
        data_list.append(d)
    return render(request, 'prev_app.html', {'data_list':data_list})
#====================================================================================
#====================================================================================