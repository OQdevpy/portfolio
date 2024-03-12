from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutList.as_view(), name="about-list"),
    path('about/<int:pk>/', views.AboutDetail.as_view(), name="about-detail"),
    path('skill/', views.SkillList.as_view(), name="skill-list"),
    path('project/', views.ProjectList.as_view(), name="project-list"),
]