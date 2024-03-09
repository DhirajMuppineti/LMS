# forms.py
from django import forms
from django_ckeditor_5.fields import CKEditor5Field
from .models import *


class ChapterForm(forms.ModelForm):
    content = CKEditor5Field()

    class Meta:
        model = Chapter
        fields = ["number", "title", "content", "course"]

        def __init__(self, *args, **kwargs):
            super(CreateCourseForm, self).__init__(*args, **kwargs)
            self.fields["course"].queryset = Course.objects.all()


class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "description", "subject", "image"]

    def __init__(self, *args, **kwargs):
        super(CreateCourseForm, self).__init__(*args, **kwargs)
        self.fields["subject"].queryset = Subject.objects.all()


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ["title", "video_file", "thumbnail", "course" ]

        def __init__(self, *args, **kwargs):
            super(CreateCourseForm, self).__init__(*args, **kwargs)
            self.fields["course"].queryset = Course.objects.all()
