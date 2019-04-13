from django.contrib import admin
from django.core.cache import cache
from .models import Article

# Easy object actions

from django_object_actions import DjangoObjectActions

# Lets label our admin site

admin.site.site_header = 'Newspaper Administration'
admin.site.site_title = 'Newspaper Administration Portal'
admin.site.index_title = 'Global Administration Portal'


@admin.register(Article)
class ArticleAdmin(DjangoObjectActions, admin.ModelAdmin):

    list_display = ['title', 'author', 'published']

    # We define our object action for publishing articles

    def publish_article(self, request, obj):
        obj.published = True  # Change state
        obj.save()
        self.message_user(request, 'Article Published')  # Notify user
        cache.clear()  # Flush cache, after we save our object

    # We define our object action for withdrawing articles

    def withdraw_article(self, request, obj):
        # Change state back to False. False is default for the published field.
        obj.published = False
        obj.save()
        self.message_user(request, 'Article Withdrawn')  # Notify user
        cache.clear()  # Flush cache, after we save our object

    # Add labels and descriptions for our object actions

    publish_article.label = "Publish"
    publish_article.short_description = "Publish this article"

    withdraw_article.label = "Withdraw"
    publish_article.short_description = "Withdraw this article"

    change_actions = ('publish_article', 'withdraw_article')
