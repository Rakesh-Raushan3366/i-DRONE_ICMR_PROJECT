from django.contrib import admin
from .models import *


# Register your models here.

class StudyAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Description', 'status', 'upload_at')
    list_display_links = ('id', 'Title')
    list_filter = ('upload_at',)
    search_fields = ('Title', 'Description')


admin.site.register(Study, StudyAdmin)


class Study_DetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'study', 'Title', 'Description', 'upload_at')
    list_display_links = ('id', 'study')
    list_filter = ('upload_at',)
    search_fields = ('Title', 'Description')


admin.site.register(Study_Details, Study_DetailsAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'study', 'News_Title', 'News_description', 'upload_at')
    list_display_links = ('id', 'study')
    list_filter = ('upload_at',)
    search_fields = ('News_Title', 'News_description')


admin.site.register(News, NewsAdmin)


class VideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'study', 'Inst_Name', 'Inst_fullname', 'Description', 'upload_at')
    list_display_links = ('id', 'study')
    list_filter = ('upload_at',)
    search_fields = ('Inst_Name', 'Inst_fullname', 'Description')


admin.site.register(Videos, VideosAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'study', 'Heading', 'Paragraph', 'upload_at')
    list_display_links = ('id', 'study')
    list_filter = ('upload_at',)
    search_fields = ('Heading', 'study')


admin.site.register(Gallery, GalleryAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Designation', 'Image', 'upload_at')
    list_display_links = ('id', 'Name')
    list_filter = ('upload_at',)
    search_fields = ('Name', 'Designation')


admin.site.register(Team, TeamAdmin)


class Idrone_TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Designation', 'Image', 'upload_at')
    list_display_links = ('id', 'Name')
    list_filter = ('upload_at',)
    search_fields = ('Name', 'Designation')


admin.site.register(Idrone_Team, Idrone_TeamAdmin)


class Research_Techanical_TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Designation', 'Image', 'upload_at')
    list_display_links = ('id', 'Name')
    list_filter = ('upload_at',)
    search_fields = ('Name', 'Designation')


admin.site.register(Research_Techanical_Team, Research_Techanical_TeamAdmin)


class Admin_IT_TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Designation', 'Image', 'upload_at')
    list_display_links = ('id', 'Name')
    list_filter = ('upload_at',)
    search_fields = ('Name', 'Designation')


admin.site.register(Admin_IT_Team, Admin_IT_TeamAdmin)


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Heading', 'Paragraph', 'upload_at')
    list_display_links = ('id', 'Heading')
    list_filter = ('upload_at',)
    search_fields = ('Heading', 'Heading')


admin.site.register(Documents, DocumentsAdmin)


class InstituteAdmin(admin.ModelAdmin):
    list_display = ('id', 'study', 'Institute_Name', 'Institute_Heading', 'Description', 'upload_at')
    list_display_links = ('id', 'study')
    list_filter = ('upload_at',)
    search_fields = ('study', 'Institute_Name')


admin.site.register(Institute, InstituteAdmin)


class Contact_usAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'message', 'upload_at')
    list_display_links = ('id', 'name')
    list_filter = ('upload_at',)
    search_fields = ('name', 'name')


admin.site.register(Contact_us, Contact_usAdmin)


class About_usAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Heading', 'upload_at')
    list_display_links = ('id', 'Title')
    list_filter = ('upload_at',)
    search_fields = ('Title', 'Heading')


admin.site.register(About_us, About_usAdmin)


class TwitterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation', 'upload_at')
    list_display_links = ('id', 'name')
    list_filter = ('upload_at',)
    search_fields = ('name', 'designation')


admin.site.register(Twitter, TwitterAdmin)


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Heading', 'upload_at')
    list_display_links = ('id', 'Title')
    list_filter = ('upload_at',)
    search_fields = ('Title', 'Heading',)


admin.site.register(Carousel, CarouselAdmin)


class StatisticAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'upload_at')
    list_display_links = ('id', 'name')



admin.site.register(Statistic, StatisticAdmin)
