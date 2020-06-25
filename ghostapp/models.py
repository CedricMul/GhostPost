from django.db import models

# Create your models here.

class GPost(models.Model):
    is_boast = models.BooleanField(default=True)
    post_text = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    date_and_time = models.DateTimeField(auto_now_add=True)
    total_votes = models.IntegerField(default=0)
    def __str__(self):
        return self.post_text