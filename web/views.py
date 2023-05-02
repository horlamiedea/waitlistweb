from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from .serializers import WaitListSerializers, RiderRegisterSerializers
from rest_framework.response import Response
from .models import WaitList
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import JsonResponse

# Create your views here.

def check_waitlist_email(email):
    if WaitList.objects.filter(email=email).exists():
        return True
    else:
        return False

class WaitListView(generics.GenericAPIView):
    
    serializer_class = WaitListSerializers
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = request.POST.get('email')
            if check_waitlist_email(email):
                return JsonResponse({'message': 'Email address already exists in waitlist.'})
            else: 
                email_from = settings.EMAIL_HOST_USER
                subject = 'Thank you for registering with us!'
                html_content = render_to_string('email.html', {'username': 'John Doe'})
                text_content = strip_tags(html_content)

                msg = EmailMultiAlternatives(subject, text_content, email_from, [email])
                msg.attach_alternative(html_content, "text/html")
                # msg.send()
                created = serializer.save()
                return Response('email sent successfully', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RiderRegisterView(generics.GenericAPIView):
    
    serializer_class = RiderRegisterSerializers
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            created = serializer.save()
            return Response('Registered successfully', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

