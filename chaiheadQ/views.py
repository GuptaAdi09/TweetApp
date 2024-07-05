from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
import smtplib
from email.message import EmailMessage
import ssl


def home(request):
    return render(request,'home.html')



def Register(request):
    form= CreateUserForm()
    if request.method == "POST":
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            print(email)
            S_email = "17aditaya@gmail.com"
            email_paa = "zmpu vrne ebcl yolb"

            receiver_email = email
        

            subject = "Welcome to Django  Based registration page "
            message = (
                     f"Hello {user},\n"
                "Welcome to our website. Thank you so much for registering with us."
            )

            em = EmailMessage()
            em["From"] =  S_email
            em["To"] = receiver_email
            em["Subject"] = subject
            em.set_content(message)
           

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(S_email, email_paa)
                smtp.sendmail(S_email, receiver_email, em.as_string())

            print("Email sent successfully")
            messages.success(request,'Account is succsesfully created for' + ' '+ user)
            return redirect('login')
            

    context_1={'f':form}
    return render(request,'register.html',context_1)
    

def Login(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')


        print(username)
        print(password)

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(reverse('tweet_list'))
        else:
            print('authentication fail')
            return redirect('register')
        
    context={}
    return render(request,'login.html',context)

