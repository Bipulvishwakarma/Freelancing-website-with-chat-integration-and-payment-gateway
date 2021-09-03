from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Customer

def customer_profile(sender,instance,created,**kwargs):
    if created:
        Customer.objects.create(
            user=instance,
            name=instance.username,

            )   

post_save.connect(customer_profile,sender=User)



