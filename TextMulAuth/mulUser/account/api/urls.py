from django.urls import include, path
from .views.students import StudentSignUpView, StudentInterestsView
from .views.teacher import TeacherSignUpView, TeacherSubjectView,SjView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),
    path('teacher/subject/', TeacherSubjectView.as_view(), name='teacher_subject'),
    path('student/subject/', StudentInterestsView.as_view(), name='student_subject'),
    path('subject_all/', SjView.as_view()),
]
