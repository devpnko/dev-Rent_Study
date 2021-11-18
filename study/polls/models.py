from django.db import models

# Create your models here.

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def __str__(self):
#         return self.question_text

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes=models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text

class ImageCollector(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField('url', blank=False, null=False)
    tags = models.CharField(max_length-100, black=True, null=True)

    def __str__(self):
        return self.title
        