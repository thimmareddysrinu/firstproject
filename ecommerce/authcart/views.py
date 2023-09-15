from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from .utils import TokenGenerator,generate_token
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.tokens import PasswordResetTokenGenerator
# Create your views here.


def signin(request):
     if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        if password != confirm_password:
            messages.warning(request, "Password is Not Matching")
            return render(request, 'signin.html')
        try:
            if User.objects.get(username=email):
               messages.info(request, "Email is Taken")
               return render(request, 'signin.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email, email, password)
        user.is_active = False
        user.save()
        email_subject = "activate your user"
        message = render_to_string('activate.html', {
            'user': 'user',
            'domain': "127.0.0.1:8000",
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        })
        email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER(email))
        email_message.save()  
        messages.success('please activate your account by the link send to your gmail')  
        return render(request, 'user created', email)
     return render(request, 'signin.html')
class ActivateAccountView(View):
          def get(self,request,token,uidb64):
               try:
                   uid=force_str(urlsafe_base64_encode(uidb64)) 
                   user=User.objects.get(pk=uid)  
               except Exception as identifer:
                    user=None
               if user is not None and generate_token.check_token(user,token):
                    user.is_active=True
                    user.save()
                    messages.info(request,"Account activated sucessfull") 
                    return redirect('auth/login') 
               return render(request,'activatefail.html')                        


def handlogin(request):
    if request.method =='POST':
         username=request.POST['email']
         userpassword=request.POST['pass1']
         myuser=authenticate(username=username,password=userpassword)
         
         if myuser is not None:
              login(request,myuser)                   
              messages.success(request,'login  sucess')  
              return redirect('/home') 
         else:
              print(' it is error')                   
              messages.error(request,"credental invalid")    
              return redirect('/auth/login')                             
    return render(request,'login.html')


def handlogout(request):
    logout(request) 
    messages.info(request,"logout sucess")                   
    return redirect('/auth/login')
