import pytest
from pytest_factoryboy import register
from ..factories import ProfileFactory, UserFactory
from account.models import Profile

register(UserFactory)
register(ProfileFactory)

pytestmark = pytest.mark.django_db


class TestProfileModel:
    def test_profile_str_method(self, profile_factory):
        profile = profile_factory.create(user__username='test_user')
        assert str(profile) == 'test_user'

    def test_profile_creation(self, profile_factory):
        profile = profile_factory()
        assert Profile.objects.count() == 1
        assert profile is not None

    def test_follows_relationship(self, profile_factory):
        profile1 = profile_factory.create(user__username='test_user')
        profile2 = profile_factory.create(user__username='test_user2')
        profile1.follows.add(profile2)
        assert profile1.follows.count() == 1
        assert profile2.follows.count() == 0

    def test_followed_by_relationship(self, profile_factory):
        profile1 = profile_factory.create(user__username='test_user')
        profile2 = profile_factory.create(user__username='test_user2')
        profile1.follows.add(profile2)
        assert profile1.followed_by.count() == 0
        assert profile2.followed_by.count() == 1
        assert profile2.followed_by.first() == profile1

    def test_profile_picture_default(self, profile_factory):
        profile = profile_factory()
        assert profile.profile_picture == 'blank-profile-picture.png'

    def test_active_default(self, profile_factory):
        profile = profile_factory()
        assert profile.active is True

    def test_inactive_profile(self, profile_factory):
        profile = profile_factory.create(active=False)
        assert profile.active is False

    def test_toggle_active_status(self, profile_factory):
        profile = profile_factory()
        assert profile.active is True
        profile.active = False
        assert profile.active is False