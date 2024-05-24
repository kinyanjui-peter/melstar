from django.db import models
"""classes for defining models"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choices(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choices_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choices_textS
