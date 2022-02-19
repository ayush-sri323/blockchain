from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.exceptions import ValidationError

class Referral(models.Model):

    referrer = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='referreds'
    )
    referred = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='referrers'
    )

    status = models.IntegerField()

    class Meta:
        unique_together = (('referrer', 'referred'),)
        ordering = ['id']
        db_table = 'referral'

    def __str__(self):
        return '{} => {}'.format(self.referrer, self.referred)

    def clean(self, *args, **kwargs):
        if self.referrer == self.referred:
            raise ValidationError(('The referrer can not be referred.'))

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Referral, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'referrals:referral_detail',
            kwargs={'pk': self.pk}
        )
