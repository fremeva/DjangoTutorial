
from django.db import models
from .user import User
from .profiles import ProjectmanagerProfile,ClientProfile,DeveloperProfile


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, default="", blank=True)
    project_manager = models.OneToOneField(ProjectmanagerProfile, blank=True, null=True, on_delete=models.CASCADE)
    client = models.ManyToManyField(ClientProfile)
    methodology = models.CharField(max_length=50)
    budget = models.BigIntegerField()
    resources = models.TextField()
    time_start_real = models.DateTimeField(blank=True, null=True)
    time_end_real = models.DateTimeField(blank=True, null=True)
    time_start_estimated = models.DateTimeField(blank=True, null=True)
    time_end_estimated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    PRIORITY = (
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low')
    )
    STATE = (
        (1, 'Done'),
        (2, 'In-progess'),
        (3, 'To-do')
    )
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField()
    requeriments = models.TextField()
    costs = models.BigIntegerField()
    estimated_target_date = models.DateTimeField(blank=True, null=True)
    responsable = models.ForeignKey(DeveloperProfile, blank=True, null=True, on_delete=models.CASCADE)
    priority = models.IntegerField(choices=PRIORITY)
    state = models.IntegerField(choices=STATE)

    def __str__(self):
        return self.project.title + " - " + self.name


class Comment(models.Model):
    task = models.ForeignKey(Task, related_name="comment")
    owner = models.ForeignKey(User, related_name="owner")
    comment = models.TextField(max_length=300)
    keyword = models.CharField(max_length=20)
    date_created = models.DateField(auto_now_add=True)

