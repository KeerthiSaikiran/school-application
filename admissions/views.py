from django.shortcuts import render
from django.http import HttpResponse

from admissions.forms import StudentModelForm, VendorForm
from admissions.models import Student


# Create your views here.

# function based views

def homepage(request):
    return render(request, 'index.html')


def add_admission(request):
    # return HttpResponse("This is admission view")
    # return render(request, 'admissions/add-admission.html', {'name': 'Saikiran', 'greeting': 'Welcome'})

    form = StudentModelForm
    studentform = {'form': form}

    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)

    return render(request, 'admissions/add-admission.html', studentform)


def admission_report(request):

    result = Student.objects.all() # get all records from the table, SELECT * FROM students
    # return HttpResponse("<h1>This is admission report view.</h1>")
    students = {'allstudents': result}
    return render(request, 'admissions/admissions-report.html', students)


def add_vendor(request):

    form = VendorForm
    vendorform = {'vendor_form': form}

    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['vendor_name'])
            print(form.cleaned_data['item'])
            print(form.cleaned_data['contact_details'])
            print(form.cleaned_data['number_of_items'])
        return homepage(request)

    return render(request, 'vendor.html', vendorform)


def delete_student(request, id):
    s = Student.objects.get(id=id)
    s.delete()

    return admission_report(request)


def update_student(request, id):
    s = Student.objects.get(id=id)
    form = StudentModelForm(instance=s)
    dict = {'form': form}

    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
        return admission_report(request)

    return render(request, 'admissions/update-admission.html', dict)