from rest_framework import serializers
from .models import *

class StudentReg(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = "__all__"

    