from modeltranslation.translator import register, TranslationOptions
from .models import About, Skill, Project

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('uz',)

@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('uz',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('uz',)
