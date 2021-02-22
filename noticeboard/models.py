from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Notice(models.Model):
    title = models.CharField("title", max_length=240)
    detail = models.TextField("detail")
    published_on = models.DateField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    fb_link = models.URLField(max_length=400, null=True, blank=True)
    attachment = models.URLField(max_length=400,  null=True, blank=True)
    CATEGORY_CHOICES = (
        ('Placements', 'Placements' ),
        ('Achievements', 'Achievements'),
        ('Examinations', 'Examinations'),
        ('Scholarships', 'Scholarships'),
        ('Activities', 'Activities'),
        ('Other', 'Other')
    )
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)

    def __str__(self):
        return str(self.published_on) +" "+ self.title

class Subscribers(models.Model):
    phone = models.CharField(unique=True,max_length=10)
    def __str__(self):
        return str(self.phone)