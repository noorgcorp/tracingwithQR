from django.db import models

# Create your models here.


class Owner(models.Model):
    pass


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    # Todo add all


class OwnerUniqueID(models.Model):
    '''
    id = IntergerField()
    owner = Owner()
    '''
    # owner
    pass


class CustomerVisits(models.Model):
    '''
    id = IntegerField()
    customer = Customer()
    date and time
    '''


'''
ds = Owner(name=deepaksshop, email, phone, city, state, add, gst)
vimal_cust = Customer(name=vimals, phone, email)
id = uniqueid(id=12345678, owner=ds)

uniqueid = 12345678
vimal_cust
may 13 11:00pm

id
paul_cust
may14 12:00am
'''
