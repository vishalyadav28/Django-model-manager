import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
STATUS_CHOICES = [
    ('trial', 'Trial'),
    ('signedup', 'Signed up'),
    ('expired', 'Expired')
]

TRIAL_DURATION = datetime.timedelta(days=30)

class AccountManager(models.Manager):
    def create_trial(self):
        account = Account(status='trial')
        account.save()
        return account

    def create_signup(self):
        account = Account(status='signedup', signup_date=timezone.now())
        account.save()
        return account

    def expire_old_trials(self):
        cutoff = timezone.now() - TRIAL_DURATION
        self.filter(status='trial', created__lte=cutoff).update(status='expired')

class Account(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, db_index=True)
    signup_date = models.DateTimeField(null=True)

    objects = AccountManager()

    def signup(self):
        assert self.status in ('trial', 'expired')
        self.status = 'signedup'
        self.signup_date = timezone.now()
        self.save()
# class BillingInfo(models.Model):
#     account = models.OneToOneField('accounts.Account', related_name='billing_info')
#     address = models.TextField()
#     card_type = models.CharField(max_length=20, choices=CARD_TYPE_CHOICES)
