from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MoodInput

class UserSerializer(serializers.ModelSerializer):
    moodinputs = serializers.PrimaryKeyRelatedField(many=True, queryset=MoodInput.objects.all())
    class Meta:
        model = User
        fields = ['id','username','moodinputs']

class MoodInputSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = MoodInput
        fields = ['user','date', 'mood', 'description','streak']