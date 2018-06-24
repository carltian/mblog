# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from  django.utils import timezone
from DjangoUeditor.models import UEditorField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.CharField(max_length =200)
    body = UEditorField(u"文章正文",height=300,width=1000,default=u'',blank=True,imagePath="uploads/blog/images/",
                           toolbars='besttome',filePath='uploads/blog/files/')
    pub_date = models.DateTimeField(default = timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title