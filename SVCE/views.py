from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from service.models import *
from django.http import JsonResponse
from transformers import GPT2Tokenizer, GPT2Config

config = GPT2Config.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2", config=config)

def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        # Generate a response using the GPT-2 model
        input_ids = tokenizer.encode(user_input, return_tensors='pt')
        output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        return JsonResponse({'response': response})

    return render(request, 'chat.html')

def Home(request):
    return render(request,'Home.html', {})

def Register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        s_name = request.POST.get('s_name')
        email = request.POST.get('email')
        phno = request.POST.get('number')
        password = request.POST.get('password')

        new_user = User.objects.create_user(name, email, password)
        new_user.phno = phno
        new_user.s_name = s_name

        new_user.save()
        return redirect('loginpage')
    return render(request,'Register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Error, user does not exist')
    return render(request,'Login.html', {})

def logoutuser(request):
    logout(request)
    return redirect('loginpage')

def Aboutus(request):
    return render(request,'Aboutus.html', {})

def Academics(request):
    return render(request,'Academics.html', {})

def Contactus(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        messages = request.POST['add']
        ins = Contact(username=username,add=messages, email=email)
        ins.save()
        print("ok")
    return render(request,'Contactus.html', {})

def CS(request):
    return render(request,'CS.html', {})

def EC(request):
    return render(request,'EC.html', {})

def IS(request):
    return render(request,'IS.html', {})

def CIVIL(request):
    return render(request,'CIVIL.html', {})

def DS(request):
    return render(request,'DS.html', {})

def CYBER(request):
    return render(request,'CYBER.html', {})

def AI(request):
    return render(request,'AI.html', {})

def MECH(request):
    return render(request,'MECH.html', {})

def Placements(request):
    return render(request,'Placements.html', {})

def Events(request):
    return render(request,'Events.html', {})

def Dash1(request):
    dashdata1 = Bookinfo.objects.all()
    if request.method=="GET":
        se=request.GET.get('searchname')
        if se!=None:
            dashdata1 = Bookinfo.objects.filter(bookname__icontains=se)
    context = {'dash1': dashdata1}
    return render(request, 'Appointmentinfo.html', context)

def Dash2(request):
    if request.method == "POST":
        bookname = request.POST['bookname']
        sem_year = request.POST['sem_year']
        link = request.POST['link']
        ins = Bookinfo(bookname=bookname,sem_year=sem_year, link=link)
        ins.save()
        print("ok")
    return render(request,'Appointmentinfo.html', {})
    