from django.db import models
from django.urls import reverse

# Import our user model, so we can attrib more than user to an Article. Like IRL.
from user.models import UserModel

"""
Add Django extensions for:
* Automatically create time stamps (created: DT field, modified: DT Field)
* Automatically generate a slug for our URLs from our title fields
"""

from django_extensions.db.models import TimeStampedModel, ActivatorModel
from django_extensions.db.fields import AutoSlugField


class Article(TimeStampedModel):
    # Fields required by test

    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()

    # If we don't default this to False, articles will be automatically published on creation
    # We also don't want it to be editable on the change form

    published = models.BooleanField(default=False, editable=False)

    # Attrib each article to a user

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='authors')

    # We use this field to automatically gen slug from title

    slug = AutoSlugField(populate_from=['title'])  # Make slug from title

    """
    Let's def the string repr of the model to make it look nice in the admin interface
    Let's also def absolute URL and create reverse lookups...
    Mostly because its complete masochism to change object URLS in the future if you dont
    And finally, let's override the save method to flush the cache on every object save as per the specs
    """

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail_view', kwargs={'slug': self.slug})  # Use slug instead of PK (Int)



