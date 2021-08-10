from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class items(models.Model):
    bought='bought'
    left='left'
    not_available='not-available'
    Choice=(
        (bought,'bought'),(left,'left'),(not_available,'not-available')
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    item_name=models.CharField(max_length=200)
    item_qun=models.CharField(max_length=200)
    status=models.CharField(choices=Choice,max_length=100,default=bought)
    date=models.DateField()