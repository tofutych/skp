from rest_framework import serializers

from .models import Group, Student



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "number", "slug", "get_absolute_url")


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("id", "group", "surname", "name", "age", "get_absolute_url")

        