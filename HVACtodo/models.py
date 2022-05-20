from django.db import models
 
class Task(models.Model):
    # Fields
    task = models.CharField(max_length = 200)
    name = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.task


