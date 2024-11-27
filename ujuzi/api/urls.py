from django.urls import path

from .views import TeacherDetailView
from .views import TeacherListView
from .views import MarkingSchemeDetailView
from .views import MarkingSchemeListView
from .views import AssessmentDetailView
from .views import AssessmentListView
from .views import FacilitatorDetailView
from .views import FacilitatorListView
from .views import ModuleDetailView
from .views import ModuleListView
from .views import KicdDetailView
from .views import KicdListView

from .views import UserListView, UserDetailView, RegisterView, LoginUser

from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
path('users/', UserListView.as_view(), name='user-list'), 
path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'), 
path('register/', RegisterView.as_view(), name='register'),  # Endpoint for user registration
path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
path('users/', UserListView.as_view(), name='all_users'),
path('user/login/', LoginUser.as_view(), name='login'), 
path("teacher/",TeacherListView.as_view(),name="teacher_list_view"),
path("teacher/<int:id>/",TeacherDetailView.as_view(),name="teacher_detail_view"),
path("markingscheme/",MarkingSchemeListView.as_view(),name="markingscheme_list_view"),
path("markingscheme/<int:id>/",MarkingSchemeDetailView.as_view(),name="markingscheme_detail_view"),
path("assessment/",AssessmentListView.as_view(),name="Assessment_list_view"),
path("Assessment/<int:id>/",AssessmentDetailView.as_view(),name="Assessment_detail_view"),
path("facilitator/",FacilitatorListView.as_view(),name="Facilitator_list_view"),
path("Facilitator/<int:id>/",FacilitatorDetailView.as_view(),name="Facilitator_detail_view"),
path("module/",ModuleListView.as_view(),name="Module_list_view"),
path("Module/<int:id>/",ModuleDetailView.as_view(),name="Module_detail_view"),
path("kicd/",KicdListView.as_view(),name="Kicd_list_view"),
path("Kicd/<int:id>/",KicdDetailView.as_view(),name="Kicd_detail_view"),


]