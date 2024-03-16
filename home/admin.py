from django.contrib import admin
from .models import About, Skill, Project, ProjectImage, Technology



class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Technology)
class ProjectTechnologyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]
    fieldsets =(
        ('Eng',{'fields':('title_en',)}),
        ('Uz',{'fields':('title_uz',)}),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    inlines = [ProjectImageInline]
    fieldsets =(
        ('Eng',{'fields':('title_en','description_en')}),
        ('Uz',{'fields':('title_uz','description_uz')}),
        ('Technology',{'fields':('techs',)}),
    )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    fieldsets =(
        ('Eng',{'fields':('title_en','description_en')}),
        ('Uz',{'fields':('title_uz','description_uz')}),
        ('Image',{'fields':('image',)})

    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    fieldsets =(
        ('Eng',{'fields':('title_en','description_en')}),
        ('Uz',{'fields':('title_uz','description_uz')}),
        ('Image',{'fields':('image',)})

    )