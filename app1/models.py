from django.db import models

class comics(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    img=models.ImageField(upload_to='comics/')
    description=models.CharField(max_length=2000)

    def __str__(self):
        return self.title  