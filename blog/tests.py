from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment


class CommentDeleteTests(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='tester', password='pass')
		self.other = User.objects.create_user(username='other', password='pass')
		self.post = Post.objects.create(title='T', slug='t', author=self.user, content='c', status=1)
		self.comment = Comment.objects.create(post=self.post, author=self.user, body='hi', approved=True)

	def test_owner_can_delete_via_post(self):
		self.client.login(username='tester', password='pass')
		url = reverse('post_detail', args=[self.post.slug]) + f'delete_comment/{self.comment.id}'
		resp = self.client.post(url)
		self.assertEqual(resp.status_code, 302)
		self.assertFalse(Comment.objects.filter(pk=self.comment.pk).exists())

	def test_non_owner_cannot_delete_ajax(self):
		self.client.login(username='other', password='pass')
		url = reverse('post_detail', args=[self.post.slug]) + f'delete_comment/{self.comment.id}'
		resp = self.client.post(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest', HTTP_ACCEPT='application/json')
		self.assertEqual(resp.status_code, 403)
		data = resp.json()
		self.assertFalse(data.get('success', True))

	def test_owner_can_edit_via_ajax(self):
		self.client.login(username='tester', password='pass')
		url = reverse('post_detail', args=[self.post.slug]) + f'edit_comment/{self.comment.id}'
		resp = self.client.post(url, data='{}', content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest', HTTP_ACCEPT='application/json')
		# empty body should be rejected
		self.assertEqual(resp.status_code, 403)

	def test_owner_can_edit_with_body_via_ajax(self):
		self.client.login(username='tester', password='pass')
		url = reverse('post_detail', args=[self.post.slug]) + f'edit_comment/{self.comment.id}'
		resp = self.client.post(url, data='{"body": "new text"}', content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest', HTTP_ACCEPT='application/json')
		self.assertEqual(resp.status_code, 200)
		data = resp.json()
		self.assertTrue(data.get('success'))
		self.assertEqual(data.get('body'), 'new text')
