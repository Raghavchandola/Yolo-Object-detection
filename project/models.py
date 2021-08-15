from os import times
from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
from django.db.models.fields.files import FileField

from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    mail = models.CharField(max_length=250)
    query = models.CharField(max_length=250)

    def __str__(self):
        return 'message from ' + self.name+' ' + self.lastname + '-- ' + self.mail


class Video(models.Model):
    video_heading = models.CharField(max_length=30)
    caption = models.TextField(max_length=400)
    video = models.FileField(upload_to='myfile')

    def __str__(self):
        return self.video_heading


class Notes(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='myfile', blank=True)
    photo_description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.heading


class Pdf(models.Model):
    pdf_heading = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='myfile')
    pdf_description = models.TextField(max_length=500)

    def __str__(self):
        return self.pdf_heading


class Chapters(models.Model):
    chapter_name = models.CharField(max_length=50)
    chapter_description = models.TextField(max_length=300)
    chapter_image = models.ImageField(upload_to='myfile')
    notes = models.ManyToManyField(Notes)
    pdf12 = models.ManyToManyField(Pdf)
    vids = models.ManyToManyField(Video)

    def __str__(self):
        return self.chapter_name


class Subjects(models.Model):
    subject_name = models.CharField(max_length=50)
    subject_description = models.TextField(max_length=500)
    chapter = models.ManyToManyField(Chapters)
    subject_image = models.ImageField(upload_to='myfile')

    def __str__(self):
        return self.subject_name


class Course(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100, default=0)
    amount = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Classes(models.Model):
    class_name = models.CharField(max_length=50)
    class_description = models.TextField(max_length=500)
    class_images = models.ImageField(upload_to='myclasses')
    class_subj = models.ManyToManyField(Subjects)
    paying = models.ManyToManyField(Course, default=0)
    create_date = models.DateTimeField(
        _('createdtimestamp'), auto_now_add=True)


class Faqs(models.Model):
    question = models.TextField(max_length=400)
    answer = models.TextField(max_length=1000)

    def __str__(self):
        return self.question


class Subj(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='myfile', blank=True)
    description = models.TextField(max_length=400)
    pdf = models.FileField(upload_to='myfile')
    video = models.FileField(upload_to='myfile')

    def _str_(self):
        return self.name
