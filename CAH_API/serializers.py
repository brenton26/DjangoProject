from rest_framework import serializers
from .models import BlackCard, WhiteCard

class BlackCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackCard
        fields = ['text','pick']


class WhiteCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhiteCard
        fields = ['text',]
