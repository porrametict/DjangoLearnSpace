from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import User, Student, Subject


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, )

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            is_student=True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',)


class TeacherSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, )

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            is_teacher=True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',)


class SubjectStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user', 'interests')


class SubjectTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'owner', 'name')

    def create(self, validated_data):
        data = Student.objects.create(
            student_id=validated_data['user'],
            subject_id=validated_data['interests']
        )
        data.save()
        return data
