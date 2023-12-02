from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(('Title'), max_length=200)
    description = models.TextField(('Description'))
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        ordering = ('title', )
        verbose_name = 'event'
        verbose_name_plural = 'events'
    
    def __str__(self):
        return str(self.title)