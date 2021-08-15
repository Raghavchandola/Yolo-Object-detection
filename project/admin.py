from functools import update_wrapper
from django.contrib import admin

# Register your models here.
from . models import Contact, Classes, Subjects, Chapters, Video, Notes, Pdf, Course, Faqs, Subj


@admin.register(Classes)
class MethodModelAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'class_images']


@admin.register(Chapters)
class ChapterModelAdmin(admin.ModelAdmin):
    list_display = ['chapter_name']
    search_fields = ['chapter_name']


@admin.register(Subjects)
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ['subject_name']
    search_fields = ['subject_name']


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'mail']
    search_fields = ['name', 'mail']


@admin.register(Video)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ['video_heading']


@admin.register(Notes)
class NotesModelAdmin(admin.ModelAdmin):
    list_display = ['heading']


@admin.register(Pdf)
class PdfModelAdmin(admin.ModelAdmin):
    list_display = ['pdf_heading']


@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'mail']
    search_fields = ['mail']


@admin.register(Faqs)
class FaqsAdmin(admin.ModelAdmin):
    list_display = ['question']


admin.site.register(Subj)
