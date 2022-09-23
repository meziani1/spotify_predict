from rest_framework import serializers 
from .models import Skipped

class SkippedSerializers(serializers.ModelSerializer): 
    class meta: 
        model=Skipped 
        fields='__all__'