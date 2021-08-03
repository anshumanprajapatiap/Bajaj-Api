from rest_framework import serializers
from BajajApi.models import Details




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Details
        fields = ['name']
