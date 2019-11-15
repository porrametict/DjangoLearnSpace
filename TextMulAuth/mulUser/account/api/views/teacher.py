from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from account.decorators import teacher_required
from rest_framework.generics import CreateAPIView,UpdateAPIView,ListAPIView
from account.api.serialzers import TeacherSerializer,SubjectTeacherSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated

from account.models import Subject


class TeacherSignUpView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = TeacherSerializer


# @method_decorator([login_required, teacher_required], name='dispatch')
class TeacherSubjectView(CreateAPIView):
    model = Subject
    permission_classes = (IsAuthenticated,)
    serializer_class = SubjectTeacherSerializer


class SjView(ListAPIView):
    model = Subject
    permission_classes = (IsAuthenticated,)
    serializer_class = SubjectTeacherSerializer
    queryset = Subject.objects.all()



