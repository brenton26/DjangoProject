from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from .models import WhiteCard, BlackCard
from .serializers import WhiteCardSerializer, BlackCardSerializer
import random


# Create your views here.
def CAH(request):
    return render(request, 'CAH_API/CAH.html')


class WhiteCards(APIView):

    def get(self, request, id=None):
        if id==None:
            cards = WhiteCard.cards.all()
            serializer = WhiteCardSerializer(cards, many=True)
            return Response(serializer.data)
        else:
            random_card_index = random.randrange(len(WhiteCard.cards.all()))
            card = WhiteCard.cards.get(id=random_card_index)
            serializer = WhiteCardSerializer(card)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = WhiteCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlackCards(APIView):

    def get(self, request, id=None):
        if id==None:
            cards = BlackCard.cards.all()
            serializer = BlackCardSerializer(cards, many=True)
            return Response(serializer.data)
        else:
            random_card_index = random.randrange(len(BlackCard.cards.all()))
            card = BlackCard.cards.get(id=random_card_index)
            serializer = BlackCardSerializer(card)
            return Response(serializer.data)

    def post(self, request):
        serializer = BlackCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

