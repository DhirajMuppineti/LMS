from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path("course/<int:course_id>/chapters/", chapter_list, name="chapter_list"),
    path(
        "course/<int:course_id>/chapter/<int:chapter_id>/edit/",
        edit_chapter,
        name="edit_chapter",
    ),
    
    path("teacher_courses/", teacher_courses, name="teacher_courses"),
    path(
        "course/<int:course_id>/create_chapter/", create_chapter, name="create_chapter"
    ),
    
    
    path("create_course/", create_course, name="create_course"),
    path("", home),

    path(
        "course/<int:course_id>/chapter/<int:chapter_id>/edit/",
        edit_chapter,
        name="edit_chapter",
    ),
    
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("home/", home, name="home"),
    path("register/", register, name="register"),
    path("course/<int:course_id>/", course_detail, name="course_detail"),
    path(
        "course/<int:course_id>/chapter/<int:chapter_id>/",
        chapter_detail,
        name="chapter_detail",
    ),
    path("teacher_courses/", teacher_courses, name="teacher_courses"),
    path('profile/', profile, name='profile'),
]
