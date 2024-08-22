from django.urls import path

from apps.users.views import UserBlockView, UserListCreateView, UserToAdminView, UserUnblockView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users-list_create'),
    path('/<int:pk>/block', UserBlockView.as_view()),
    path('/<int:pk>/un_block', UserUnblockView.as_view()),
    path('/<int:pk>/admins', UserToAdminView.as_view()),
    ]