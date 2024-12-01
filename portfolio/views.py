from django.shortcuts import render
from .models import PersonalInfo, WorkExperience, Skill

def index(request):
    personal_info = PersonalInfo.objects.first()
    # work_experience = WorkExperience.objects.all()
    # skills = Skill.objects.all()
    return render(request, 'index.html', {
        'personal_info': personal_info,
        # 'work_experience': work_experience,
        # 'skills': skills,
    })
