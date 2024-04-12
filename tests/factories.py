import factory
from django.contrib.auth.models import User
from account.models import Profile
from feed.models import Post, Comment


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    bio = factory.Faker('text', max_nb_chars=200)
    date_of_birth = factory.Faker('date_of_birth')


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence', nb_words=4)
    content = factory.Faker('paragraph')
    author = factory.SubFactory(UserFactory)


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    content = factory.Faker('paragraph')
    author = factory.SubFactory(UserFactory)
    posts = factory.SubFactory(PostFactory)
