from django.shortcuts import render
from django.views import generic
from rest_framework import status, viewsets, filters
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Member, Position, MemberPosition
from .serializers import MemberSerializer, PositionSerializer, ListMemberPositionSerializer, PostMemberPositionSerializer

class GetTestAPI(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response(data={'status': 'Hello World!!!'}, status=status.HTTP_200_OK)

# MemberのList取得
class ListMembers(generics.ListAPIView):
    """ View to list all members"""
    queryset = Member.objects.all().order_by('member_id')
    serializer_class = MemberSerializer
    # permission_classes = (permissions.IsAuthenticated,)

# Memberの作成API
class CreateMember(generics.CreateAPIView):
    """ View to create a new Member. Only accepts POST requests """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

# PositionのList取得
class ListPositions(generics.ListAPIView):
    """ View to list all Positions"""
    queryset = Position.objects.all().order_by('position_id')
    serializer_class = PositionSerializer
    # permission_classes = (permissions.IsAuthenticated,)

# Positionの作成API
class CreatePosition(generics.CreateAPIView):
    """ View to create a new Position. Only accepts POST requests """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

# MemberPositionのList取得
class ListMemberPositions(generics.ListAPIView):
    """ View to list all MemberPositions"""
    queryset = MemberPosition.objects.all().order_by('position_id')
    serializer_class = ListMemberPositionSerializer
    # permission_classes = (permissions.IsAuthenticated,)

# MeberPositionの作成API
class CreateMemberPosition(generics.CreateAPIView):
    """ View to create a new MemberPosition. Only accepts POST requests """
    queryset = MemberPosition.objects.all()
    serializer_class = PostMemberPositionSerializer