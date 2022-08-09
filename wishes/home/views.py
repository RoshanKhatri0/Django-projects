from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from .models import detail
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template import loader
from django.urls import reverse


# Create your views here.
def index(request):
    context = {'success': False}
    if request.method == 'POST':
        Name = request.POST['Name']
        Date = request.POST['Date']
        Message = request.POST['Message']
        Email = request.POST['Email']
        new_bd = detail(Name=Name, Date=Date, Message=Message, Email=Email)
        new_bd.save()
        context = {'success': True}
    return render(request, 'index.html',context)

def data(request, bd_id = 0):
    bds = detail.objects.all()
    context = {
        'bds': bds 
    }
    print(context)

    return render (request,'data.html', context)

def delete_data(request, bd_id):
    data = detail.objects.get(pk=bd_id)
    data.delete()
    return redirect('data')

def edit(request, id):
  bds = detail.objects.get(id=id)
  template = loader.get_template('edit.html')
  context = {
    'bds': bds
  }
  return HttpResponse(template.render(context, request))
    
def edit_data(request, id):

  Name = request.POST['Name']
  Date = request.POST['Date']
  Message = request.POST['Message']
  Email = request.POST['Email']

  data = detail.objects.get(id = id)
  data.Name = Name
  data.Date = Date
  data.Message = Message
  data.Email = Email
  data.save()
  return HttpResponseRedirect(reverse('data'))