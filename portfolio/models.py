from django.db import models


class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=100, default='assets/portrait.jpg')
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    map_iframe = models.TextField(max_length=1000, blank=True, null=True) 

    def __str__(self):
        return self.name
    

class WorkExperience(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
    

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(help_text="Enter a value between 0 and 100")
    color_code = models.CharField(max_length=7, help_text="Enter a hex color code, e.g., #ff5733")

    def __str__(self):
        return self.name
    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100, default="matej")

    def __str__(self):
        return self.title
    

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    

class Theme(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
    theme = models.CharField(max_length=10, choices=[('light', 'Light'), ('dark', 'Dark')], default='light')

    def __str__(self):
        return f"Theme preference: {self.theme}"
