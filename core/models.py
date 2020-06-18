from django.db import models
from users.models import User
from django.db.models import Q


class Question(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="questions"
    )
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=500)
    asked_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name="answers")
    question = models.ForeignKey(
        to=Question, on_delete=models.CASCADE, related_name="answers"
    )
    body = models.CharField(verbose_name="Response", max_length=500)
    answered_on = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.body
