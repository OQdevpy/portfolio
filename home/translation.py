from modeltranslation.translator import register, TranslationOptions
from .models import About, Skill, Project, Technology

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('en',)

@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('en',)

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('en',)

@register(Technology)
class TechnologyTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('en',)