import pytest
from pytest_factoryboy import register
from feed.models import Post, Comment
from ..factories import ProfileFactory, UserFactory, PostFactory, CommentFactory

register(UserFactory)
register(ProfileFactory)
register(PostFactory)
register(CommentFactory)

pytestmark = pytest.mark.django_db


class TestPostModel:

    def test_post_str_method(self, post_factory):
        post = post_factory.create(title='Test Post')
        assert str(post) == 'Test Post'

    def test_post_creation(self, post_factory):
        post = post_factory()
        assert Post.objects.count() == 1
        assert post is not None

    def test_number_of_likes(self, post_factory, user_factory):
        post = post_factory()
        user1 = user_factory()
        user2 = user_factory()
        user3 = user_factory()
        assert post.likes.count() == 0
        post.likes.add(user1)
        post.likes.add(user2)
        post.likes.add(user3)
        assert post.likes.count() == 3

    def test_post_absolute_url(self, post_factory):
        post = post_factory()
        assert post.get_absolute_url() == f'/feed/detail_post/{post.id}/'

    def test_post_ordering(self, post_factory):
        post1 = post_factory()
        post2 = post_factory()
        assert Post.objects.first() == post2
        assert Post.objects.last() == post1

    def test_post_update(self, post_factory):
        post = post_factory()
        post.title = 'Updated Title'
        post.save()
        assert post.title == 'Updated Title'

    def test_post_delete(self, post_factory):
        post = post_factory()
        post.delete()
        assert Post.objects.count() == 0


class TestCommentModel:

    def test_comment_str_method(self, comment_factory):
        comment = comment_factory.create(content='Test Comment')
        assert str(comment) == 'Test Comment'

    def test_comment_creation(self, comment_factory):
        comment = comment_factory()
        assert Comment.objects.count() == 1
        assert comment is not None

    def test_number_of_likes(self, comment_factory, user_factory):
        comment = comment_factory.create(content='Test Comment')
        user1 = user_factory()
        user2 = user_factory()
        user3 = user_factory()
        assert comment.likes.count() == 0
        comment.likes.add(user1)
        comment.likes.add(user2)
        comment.likes.add(user3)
        assert comment.likes.count() == 3

    def test_edit_comment(self, comment_factory):
        comment = comment_factory()
        new_content = "Updated Comment"
        comment.content = new_content
        comment.save()
        assert comment.content == new_content

    def test_delete_comment(self, comment_factory):
        comment = comment_factory()
        comment.delete()
        assert Comment.objects.count() == 0
