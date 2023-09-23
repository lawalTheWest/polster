from django.db import models


class Questions(models.Model):
    '''
        This class defines the question Class
        It inherits from the base model class
    '''
    question_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    '''
        this defines the question choices
    '''
    # if a question is deleted, the choices should be deleted alongside
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text