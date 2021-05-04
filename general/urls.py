from constituent_operations.views import GetUserInfoView
from django.urls import path
from .views import *
from superadmin_operations.views import RetrieveActionPlanSwitchStatus


urlpatterns = [
    path("send-message/", SendMessageMPView.as_view(), name="send_message"),
    path("get-user-info/<id>/", GetUserInfoView.as_view(), name="user_info"),
    path("get-actionplan-status/", RetrieveActionPlanSwitchStatus.as_view(), name="actionplan_status"),
    path("edit-profile/<id>/", EditProfileView.as_view(), name="edit_profile")
]
