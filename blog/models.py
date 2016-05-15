import datetime

from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


tweet = 1000

class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_day = models.DateTimeField('pub date')
    text = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > tweet:
            return self.text[:tweet]
        else:
            return self.text

    def w_p_r(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_day <= now
    w_p_r.admin_order_field = 'pub_date'
    w_p_r.boolean = True
    w_p_r.short_description = 'fresh'
