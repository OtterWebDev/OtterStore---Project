
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import User, UserCustomer, UserVendor


@receiver (post_save,sender=User)
def post_save_create_user_customer(sender,instance,created,**kwargs):
    
    if created :
        if instance.role == 2:
            UserCustomer.objects.create(user=instance)
    
        if instance.role == 1:
            UserVendor.objects.create(user=instance)                   
    else:
        try:
            if instance.role == 2:
                customer_profile = UserCustomer.objects.get(user=instance)            
                customer_profile.save()     
                 
            if instance.role == 1:
                vendor_profile = UserVendor.objects.get(user=instance)            
                vendor_profile.save() 
                      
        except:
            if instance.role == 2:
                UserCustomer.objects.create(user=instance)
                
            if instance.role == 1:
                UserVendor.objects.create(user=instance)
                
                

