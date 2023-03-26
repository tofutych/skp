from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Group, Student
from .serializers import GroupSerializer, StudentSerializer


class GroupDetail(APIView):
    def get_object(self, id):
        try:
            return Group.objects.get(id=id)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        group = self.get_object(id)
        serializer = GroupSerializer(group)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        group = self.get_object(id)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        group = self.get_object(id)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupList(APIView):
    def get(self, request, format=None):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        student = self.get_object(id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        student = self.get_object(id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentsList(APIView):
    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentsByGroupList(APIView):
    def get(self, request, id, format=None):
        students = Student.objects.filter(group__id=id)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class StudentsByGroupSlugList(APIView):
    def get(self, request, slug, format=None):
        students = Student.objects.filter(group__slug=slug)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
