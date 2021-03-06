from django.db import models
from datetime import datetime 
# Create your models here.

CHOICE = (('1','CC, KEYSTONE,DASHBOARD,GLANCE'),('2','NC'))

class Hosts(models.Model):
    hostname = models.CharField(max_length=20,primary_key=True, blank=False)
    static_ip = models.CharField(max_length=20)
    dhcp_ip = models.CharField(max_length=20)
    timestamp = models.DateTimeField(default=datetime.now,blank=True)
    status = models.CharField(max_length=20, null=True)
    role = models.CharField(max_length=50, choices=CHOICE, null=True)

    def __str__(self):
        return self.hostname

    class Meta:
        ordering = ["hostname"]
