from rest_framework import serializers
from . models import User_Model, Activity_Period_Model


class User_Model_serializer(serializers.ModelSerializer):

    username = serializers.CharField(read_only=True)

    class Meta:

        model = User_Model
        fields = '__all__'

class Activity_Period_Model_serializer(serializers.ModelSerializer):

    username = serializers.CharField(source='username.username', read_only=True)

    class Meta:

        model = Activity_Period_Model
        fields = ('username','start_time','end_time')




