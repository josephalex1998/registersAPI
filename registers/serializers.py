from rest_framework import serializers
from registers.models import Registers

class RegistersSerializer(serializers.ModelSerializer):


    class Meta:
        model = Registers
        fields = ('id','name','email','phone','password','confirmPassword')