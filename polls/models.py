from django.db import models


class Question(models.Model):
    q_text = models.CharField(max_length=200)
    published = models.DateTimeField('date published')

    def __str__(self):
        return self.q_text


class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
