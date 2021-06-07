from rest_framework import serializers
from .models import Member, Position, MemberPosition

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = (
            'member_id',
            'last_name',
            'first_name',
            'nick_name',
            'number'
        )

class PositionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Position
        fields = (
            'position_id',
            'position_name'
        )

class ListMemberPositionSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    position = PositionSerializer()
    
    class Meta:
        model = MemberPosition
        fields = (
            'member_position_id',
            'member',
            'position',
            'position_level'
        )

class PostMemberPositionSerializer(serializers.ModelSerializer):
    member = serializers.PrimaryKeyRelatedField(queryset=Member.objects.all())
    position = serializers.PrimaryKeyRelatedField(queryset=Position.objects.all())
    
    class Meta:
        model = MemberPosition
        fields = (
            'member_position_id',
            'member',
            'position',
            'position_level'
        )
