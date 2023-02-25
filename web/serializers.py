from rest_framework.serializers import ModelSerializer, Serializer
from .models import WaitList, RiderRegister

class WaitListSerializers(ModelSerializer):
    class Meta:
        
        model = WaitList
        fields = '__all__'
        

class RiderRegisterSerializers(ModelSerializer):
    
    class Meta:
        model = RiderRegister
        fields = '__all__'