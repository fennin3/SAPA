from users.models import Area, Constituency
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Comment(models.Model):
    text = models.CharField(max_length=500)
    comment_from = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Comment from {self.comment_from.full_name}"
    


class Project(models.Model):
    mp = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=20000)
    place = models.CharField(max_length=10000)
    media = models.FileField(upload_to="mp_projects/", null=True,blank=True)
    description = models.CharField(max_length=1000000)
    comments = models.ManyToManyField(Comment, blank=True, null=True, related_name="project")
    likes = models.ManyToManyField(User,related_name="likes", null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return self.name


class ActionPlanAreaSummaryForMp(models.Model):
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="action_plan/")
    comment = models.CharField(max_length=20000, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

class AverageActionPlanStat(models.Model):
    title = models.CharField(max_length=200)
    total_number = models.IntegerField()
    total_value = models.IntegerField()
    date = models.DateField(auto_now_add=True)








