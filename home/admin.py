from django.contrib import admin
from .models import About, Skill, Project, ProjectImage



class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    inlines = [ProjectImageInline]
    fieldsets =(
        ('Uz',{'fields':('title_uz','description_uz')}),
        ('Eng',{'fields':('title_en','description_en')}),
        ('Ru',{'fields':('title_ru','description_ru')}),
    )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    fieldsets =(
        ('Uz',{'fields':('title_uz','description_uz')}),
        ('Eng',{'fields':('title_en','description_en')}),
        ('Ru',{'fields':('title_ru','description_ru')}),
        ('Image',{'fields':('image',)})

    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    fieldsets =(
        ('Uz',{'fields':('title_uz','description_uz')}),
        ('Eng',{'fields':('title_en','description_en')}),
        ('Ru',{'fields':('title_ru','description_ru')}),
        ('Image',{'fields':('image',)})

    )