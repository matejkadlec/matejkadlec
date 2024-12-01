from django.contrib import admin
from .models import PersonalInfo, WorkExperience, Skill, BlogPost, ContactForm, Theme

admin.site.register(PersonalInfo)
admin.site.register(WorkExperience)
admin.site.register(Skill)
admin.site.register(BlogPost)
admin.site.register(ContactForm)
admin.site.register(Theme)
