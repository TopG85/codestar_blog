from django.db import models


class CollabRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    project_name = models.CharField(max_length=255, blank=True)
    project_description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.name} - {self.project_name or 'No title'}"
