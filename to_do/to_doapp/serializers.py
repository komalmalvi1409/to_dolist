from .models import To_doo
from .models import Login

from rest_framework import serializers

class To_dooSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = To_doo
        fields = ['url','title', 'description','category','duedate']

class LoginSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Login
        fields = ['url','email', 'password']
