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


# class ProfileSerializer(serializers.ModelSerializer):
#     user = serializers.Field(source='user.username')

#     class Meta:
#         model = Profile
#         fields = ('id', 'name', 'active', 'type', 'user')

# class StationSerializer(serializers.ModelSerializer):
#     station = serializers.CharField(read_only=True)

#     class Meta:
#         model = Station


# class FlatSerializer(serializers.ModelSerializer):
#     station_name = serializers.CharField(source='station.name', read_only=True)

#     class Meta:
#         model = Flat
#         fields = ('station_name', )

