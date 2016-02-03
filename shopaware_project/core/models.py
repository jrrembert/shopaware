from django.db import models

from jsonfield import JSONField


class CoreAbstractBaseModel(models.Model):

    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Places(CoreAbstractBaseModel):

    is_active = models.BooleanField(default=True)
    description = models.TextField(max_length=1000) # Not validated by db
    website = models.URLField(max_length=2048)
    # tags = models.ManyToManyField('insert tag model')
    # spatial = models.JSONField()
