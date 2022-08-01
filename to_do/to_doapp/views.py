from django.shortcuts import render
from django.http import HttpResponse
from .models import Login
from .models import To_doo
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.views.generic.edit import FormView
from django.views.generic.edit import DeleteView
from rest_framework import viewsets
from rest_framework import permissions
from to_doapp.serializers import To_dooSerializer
from to_doapp.serializers import LoginSerializer

class To_dooViewSet(viewsets.ModelViewSet):


    queryset = To_doo.objects.all()

    serializer_class =  To_dooSerializer

class LoginViewSet(viewsets.ModelViewSet):


    queryset = Login.objects.all()

    serializer_class =  LoginSerializer








def login(request):
    if request.method=="POST":
        d=Login(email=request.POST["email"],password=request.POST["password"])
        d.save()
        
        return render(request,"to_doapp/to_doo_form.html")
    return render(request,"to_doapp/home.html")


class To_dooCreate(CreateView):
	model = To_doo
	fields = ['title', 'description','category','duedate']
	success_url = '/to_doapp/to_doolist'

class To_dooList(ListView):
	model =To_doo


class To_dooUpdate(UpdateView):
	model = To_doo
	fields = ['title', 'description','category','duedate']
	success_url = '/to_doapp/to_doolist'

class To_dooDelete(DeleteView):
	model =To_doo
	success_url = '/to_doapp/to_doolist'       