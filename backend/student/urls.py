from django.urls import path

from student import views

urlpatterns = [
    path("groups/", views.GroupList.as_view()),
    path("groups/<int:id>/", views.GroupDetail.as_view()),
    # path("groups/<int:id>/students", views.StudentsByGroupList.as_view()),
    path("groups/<slug:slug>/students", views.StudentsByGroupSlugList.as_view()),
    path("students/", views.StudentsList.as_view()),
    path("students/<int:id>/", views.StudentDetail.as_view()),
]