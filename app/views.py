from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    TFO=TopicForm()
    d={'form':TFO}


    if request.method=='POST':
        fd=TopicForm(request.POST)
        if fd.is_valid():
            tn=fd.cleaned_data['topic_name']
            T=Topic.objects.get_or_create(topic_name=tn)[0]
            T.save()
        return HttpResponse('topic is inserted')
    return render(request,'insert_topic.html',d)
