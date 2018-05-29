from django.db import models
import datetime
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.
class Page(models.Model):
    page_title = models.CharField(max_length=30)
    page_url = models.URLField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.page_title
    def was_published_recently(self):
       now = timezone.now()
       return now - datetime.timedelta(days = 1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'

class PageContent(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    content_text = HTMLField()

    def __str__(self):
        return self.content_text
