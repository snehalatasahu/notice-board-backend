from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Notice, Subscribers
from .serializers import *
from twilio.rest import Client 

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.

@api_view((['GET']))
def notice(request , category):
    if request.method == 'GET':
        c = category.capitalize()
        data = Notice.objects.filter(category=c).order_by('-id')

        serializer = NoticeSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

@api_view((['POST']))
def whatsapp(request):
    if request.method == 'POST':
        serializer = SubscribersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            sendWelcomeMsg()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@staff_member_required
def addNotice(request):
    return render(request, "myapp/template/hello.html")


@receiver(post_save, sender=Notice)
def sendMsg(sender,instance, **kwargs):
    account_sid = 'AC82da6297641708ee95f5fc5d02e9b90f' 
    auth_token = '81a7609a1430638612c446aa0b6aeeef' 
    client = Client(account_sid, auth_token) 
    phone = [ph.phone for ph in Subscribers.objects.all()]

    if instance.fb_link!=None:
        flink = '\n\U0001F447\nCheckout the link for more info- '+instance.fb_link
    else:
        flink = ''
    if instance.attachment!=None:
        alink = '\n\U0001F447\nAttached file- '+instance.attachment
    else:
        alink = ''

    for ph in phone:
    
        message = client.messages.create( 
                                    from_='whatsapp:+14155238886',  
                                    body='New from '+instance.category+' Notices!!\n\U0001F53B\n'+'_*"'+instance.title+'"*_ '+flink+alink,      
                                    to='whatsapp:+91{}'.format(ph)
                                ) 
 
        print(message.sid, instance.category)

def sendWelcomeMsg():
    account_sid = 'AC82da6297641708ee95f5fc5d02e9b90f' 
    auth_token = '81a7609a1430638612c446aa0b6aeeef' 
    client = Client(account_sid, auth_token) 
    ph = Subscribers.objects.last().phone



    message = client.messages.create( 
                                    from_='whatsapp:+14155238886',  
                                    body='Welcome to CET Notice Board Space! \U0001F60A',      
                                    to='whatsapp:+91{}'.format(ph)
                                ) 
 


