from django.db import models
from django.contrib.auth.models import User

from jsonfield import JSONField


class CoreAbstractBaseModel(models.Model):

    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Places(CoreAbstractBaseModel):

    created_by = models.ForeignKey(User,
                                   related_name='places',
                                   editable=False)
    is_active = models.BooleanField(default=True)
    description = models.TextField(max_length=1000) # Not validated by db
    website = models.EmailField(max_length=254)
    # tags = models.ManyToManyField('insert tag model')
    # spatial = models.JSONField()

    def __str__(self):
        return "%s (%s)".format(self.name, self.website)
