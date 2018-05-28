from django.db import models

# Create your models here.
class Page(models.Model):
    page_title = models.CharField(max_length=30)
    page_url = models.URLField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.page_title

class PageContent(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    content_text = models.CharField(max_length=250)

    def __str__(self):
        return self.content_text
