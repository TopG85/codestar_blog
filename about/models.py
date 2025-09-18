from django.db import models
from django_summernote.fields import SummernoteTextField


class About(models.Model):
	"""Single About record for the site (edited by superuser only)."""
	title = models.CharField(max_length=255)
	content = SummernoteTextField(blank=True)
	# Optional date/time to display on the About page (set manually in admin)
	display_datetime = models.DateTimeField(null=True, blank=True)
	updated_on = models.DateTimeField(auto_now=True)
	created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		pass

	def __str__(self):
		return self.title

