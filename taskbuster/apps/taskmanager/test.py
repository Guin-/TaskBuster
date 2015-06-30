# -*- # -*- coding: utf-8 -*-
from django.test import TestCase

from django.contrib.auth import get_user_model
from . import models

class TestProfileModel(TestCase):

    def test_profile_creation(self):
        # get_user_model gets a custom User Model if defined or displays
        # Djangos default user model
        User = get_user_model()
        # New User created
        user = User.objects.create(
            username= "taskbuster", password="django-tutorial")
        # Check that a profile instance has been created
        self.assertIsInstance(user.profile, models.Profile)
        # Call the save method of the user to activate the
        # signal again and check that it doesn't try to create a
        # second profile instance
        user.save()
        self.assertIsInstance(user.profile, models.Profile)


