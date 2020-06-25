from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from normalview.models import Messages
from normalview.forms import MessagesForm

# Create your views here.
from django.views import View
from django.views.generic import CreateView


class NormalHome(View):
    def get(self,request):
        return render(request, 'home.html')


class MessageView(CreateView):
    def get(self,request):
        form = MessagesForm()
        return render(request,'message.html',{'form':form})

    def post(self,request):
        form = MessagesForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['from_mail']
            mess = form.cleaned_data['message']
            m1 = Messages.objects.create(from_mail=email,message=mess)
            m1.save()
            return render(request,'message.html',{'komunikat':'Message sended.','form':form})
        return render(request, 'message.html', {'komunikat': 'Error', 'form': form})