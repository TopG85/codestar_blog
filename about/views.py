from django.shortcuts import render
from .models import About


def about_me(request):
	"""Render the About page using the most recently updated About record."""
	about = About.objects.all().order_by('-updated_on').first()
	return render(
		request,
		'about/about.html',
		{'about': about},
	)
