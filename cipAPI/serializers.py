from django.contrib.auth.models import User, Group
from adjustHT.cipAPI.models import Adjdata
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ADJSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adjdata
        fields = ['date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue']