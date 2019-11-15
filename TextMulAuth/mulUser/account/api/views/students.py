from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from account.decorators import student_required
from rest_framework.generics import CreateAPIView,UpdateAPIView,ListAPIView
from account.api.serialzers import UserSerializer,SubjectStudentSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated

from account.models import Student


class StudentSignUpView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


@method_decorator([login_required, student_required], name='dispatch')
class StudentInterestsView(CreateAPIView):
    model = Student
    permission_classes = (IsAuthenticated,)
    serializer_class = SubjectStudentSerializer




