from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=128, null=False)
    home_no = models.CharField(max_length=20, null=True)
    mobile_no = models.CharField(max_length=20, null=True)
    address = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['full_name']
