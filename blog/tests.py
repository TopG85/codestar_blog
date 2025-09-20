from django.test import TestCase
from django.urls import reverse


class SmokeTests(TestCase):
	def test_index_loads(self):
		"""Simple smoke test: index page returns 200"""
		resp = self.client.get(reverse('index'))
		self.assertEqual(resp.status_code, 200)
