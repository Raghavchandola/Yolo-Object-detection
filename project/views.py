import project
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import razorpay
import matplotlib as plt

from . models import Chapters, Classes, Contact, Subjects, Course, Faqs, Subj


# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        User = auth.authenticate(username=username, password=password)
        if User is not None:
            auth.login(request, User)

            return redirect('home')

        else:
            messages.success(request, 'Check your Username and Password')
            return redirect('/')
    else:
        return render(request, 'project/login.html')


def signuppage(request):
    if request.method == 'POST':
        username = request.POST['urname']
        name = request.POST['name']
        mail = request.POST['mail']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        punctions = '''!"#$%&'()*+, -/:;<=>?[\]^_`{|}~'''
        if User.objects.filter(username=username).exists():

            messages.error(request, 'Username already exists')
            return redirect('signuppage')
        if User.objects.filter(email=mail).exists():
            messages.error(request, 'mail already exists')
            return redirect('signuppage')

        for i in username:
            if i not in punctions:
                pass
            else:
                messages.error(
                    request, 'Symbols and Space not allowed in username')
                return redirect('signuppage')

        if len(username) <= 5:
            messages.error(
                request, 'Username should contain minimum 6 Character')
            return redirect('signuppage')

        if len(password1) <= 4:
            messages.error(
                request, 'Choose a strong password having minimum 5 character')
            return redirect('signuppage')

        if password1 != password2:
            messages.error(
                request, "Password you entered first didn't get match")
            return redirect('signuppage')
        else:
            myuser = User.objects.create_user(username, mail, password1)
            myuser.first_name = name
            myuser.save()
            return render(request, 'project/login.html')

    else:
        return render(request, 'project/signup.html')


def home(request):
    return render(request, 'project/home.html')


def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect('/')


def contact(request):
    if request.method == 'POST':
        name = request.POST['fname1']
        lname = request.POST['lname1']
        mail = request.POST['mail12']
        query = request.POST['query']
        contact = Contact(name=name, lastname=lname, mail=mail, query=query)
        contact.save()
        messages.success(request, 'Your Query Successfully submitted')
        return redirect('contact')

    else:
        return render(request, 'project/contact.html')


def classes(request,):
    object123 = Classes.objects.all()

    return render(request, 'project/classes.html', {'show': object123})


def paying(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = int(request.POST.get('amount'))*100
        client = razorpay.Client(
            auth=("rzp_test_FNd5RWpbQM20Ab", "DdoDnQvmpnHUkNe3gJq6A3d8"))
        payment = client.order.create(
            {'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

        course = Course(name=name, amount=amount/100, payment_id=payment['id'])
        course.save()
        return render(request, 'project/paying.html', {'payment': payment})

    return render(request, 'project/paying.html')

def graph():
    data=[6,4,2,1]
    return(data)

@csrf_exempt
def success(request):
    if request.method == 'POST':
        a = request.POST
        order_id = " "
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        user = Course.objects.filter(payment_id=order_id).first()
        print(user)
        print(order_id)
        user.paid = True
        user.save()
        object123 = Classes.objects.all()
        if user.paid == True:
            return redirect('classes')
        return render(request, 'project/classes.html', {'show': object123})


def opened_dash(request, pk_test):
    classes = Classes.objects.filter(id=pk_test)

    return render(request, 'project/opened_class.html', {'data': classes})


def opened_subject(request, test):
    subject = Subjects.objects.filter(id=test)

    return render(request, 'project/opened_subject.html', {'sub': subject})


def opened_chapter(request, sub_test):
    chapter = Subjects.objects.filter(id=sub_test)

    return render(request, 'project/opened_chapter.html', {'chapter': chapter})


def opened_notes(request, sub):
    alldata = Chapters.objects.filter(id=sub)

    return render(request, 'project/opened_notes.html', {'data12': alldata})


@csrf_exempt
def faq(request):
    object123 = Faqs.objects.all()

    return render(request, 'project/faq.html', {'show': object123})


def test(request):

    return render(request, 'project/test.html')


def test1(request):
    if request.method == "POST":
        name = request.POST['number']
        print(name)
        res = int(name)
        if res >= 40:
            return redirect('certificate')
        return render(request, 'project/test1.html', {'dict1': res})


def certificate(request):
    return render(request, 'project/certificate.html')


def level(request):
    return render(request, 'project/level.html')


def accent(request):
    return render(request, 'project/accent.html')


def opening(request):
    obj = Subj.objects.all
    return render(request, 'project/opening.html', {'product': obj})


def displaying(request, pk):
    objects = Subj.objects.get(id=pk)
    return render(request, 'project/display.html', {'display': objects})


def initial(request):
    return render(request, 'project/initial.html')
