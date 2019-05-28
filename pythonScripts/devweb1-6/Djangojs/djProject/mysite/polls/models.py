from  django.db import models
from  django.utils import  timezone
from    datetime   import  timedelta

# Create your models here.
class  Question(models.Model):
  question_text = models.CharField(max_length=200)
  publish_date = models.DateTimeField('date  published')

  def  __str__(self):
    return  self.question_text
  def  was_publish_recently(self):
    return  self.publish_date > timezone.now() - timedelta(days=7)
    #最近七天发布的信息

class  Choice(models.Model):
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)

  def  __str__(self):
    return  self.choice_text


