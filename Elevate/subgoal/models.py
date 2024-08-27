from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Subgoal(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('I', 'In Progress'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='subgoals')
    title = models.CharField(max_length=255)  
    deadline = models.DateTimeField()  #
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P') 
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')  
    created_at = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.title