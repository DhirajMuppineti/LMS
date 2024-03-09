from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


@login_required
def create_course(request):
    if request.method == "POST":
        form = CreateCourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            profile = Profile.objects.get(user=request.user.id)
            teacher = Teacher.objects.get(teacher=profile)
            course.teacher = teacher
            course.save()
            return redirect("teacher_courses")
    else:
        form = CreateCourseForm()

    return render(request, "create_course.html", {"form": form})


@login_required
def create_chapter(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.course_id = course_id
            chapter.save()
            return redirect("chapter_list", course_id=course_id)
    else:
        form = ChapterForm()

    return render(
        request, "create_chapter.html", {"form": form, "course_id": course.id}
    )


@login_required
def add_lesson(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            return redirect("chapter_list", course_id=course.id)
    else:
        form = LessonForm()

    return render(request, "add_lesson.html", {"form": form, "course": course})


@login_required
def watch_lesson(request, course_id, lesson_id):
    course = get_object_or_404(Course, id=course_id)
    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)

    return render(request, "watch_lesson.html", {"course": course, "lesson": lesson})


@login_required
def chapter_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    chapters = Chapter.objects.filter(course=course)
    lessons = Lesson.objects.filter(course=course)
    return render(
        request, "chapter_list.html", {"course": course, "chapters": chapters, "lessons":lessons}
    )


@login_required
def edit_chapter(request, course_id, chapter_id):
    course = get_object_or_404(Course, id=course_id)
    chapter = get_object_or_404(Chapter, id=chapter_id, course=course)

    if request.method == "POST":
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect("chapter_list", course_id=course.id)
    else:
        form = ChapterForm(instance=chapter)

    return render(
        request,
        "edit_chapter.html",
        {"form": form, "course": course, "chapter": chapter},
    )


# Views
@login_required
def home(request):
    courses = Course.objects.all()
    return render(request, "index.html", {"courses": courses})


@login_required
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    chapters = Chapter.objects.filter(course=course)
    lessons = Lesson.objects.filter(course=course)
    return render(
        request,
        "course.html",
        {"course": course, "chapters": chapters, "lessons":lessons},
    )


@login_required
def teacher_courses(request):
    current_user_profile = request.user.profile
    teachers = Teacher.objects.filter(teacher=current_user_profile)

    if teachers.exists():
        # The current user is a teacher
        courses = Course.objects.filter(teacher=teachers[0])
        return render(request, "teacher_courses.html", {"courses": courses})
    else:
        return HttpResponseForbidden("You are not registered as a teacher.")


@login_required
def chapter_detail(request, course_id, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    return render(request, "chapters.html", {"chapter": chapter})

@login_required
def profile(request):
    return render(request, 'profile.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})
