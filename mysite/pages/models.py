from django.db import models
import datetime
from django.utils import timezone
from django.template.defaultfilters import truncatechars

# Create your models here.
class Page(models.Model):
    page_title = models.CharField(max_length=30)
    page_url = models.URLField(unique=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.page_title
    @property
    def link(self):
        return self.page_url

    def was_published_recently(self):
       now = timezone.now()
       return now - datetime.timedelta(days = 1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'

class PageContent(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    content_text = models.TextField()

    def __str__(self):
        return truncatechars(self.content_text, 50)
        #return self.content_text

    @property
    def short_description(self):
        return truncatechars(self.content_text, 50)

class PageMenu(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    menu = models.CharField(max_length=30)
    menu_image = models.ImageField()

class MenuLink(models.Model):
    menu = models.ForeignKey(PageMenu, on_delete=models.CASCADE)
    link = models.ForeignKey(Page, to_field='page_url', on_delete=models.CASCADE)

    