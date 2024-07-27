from django.db import models
class customer(models.Model):
    branch_code=models.IntegerField()
    branch_name=models.CharField(max_length=15)
    customer_name=models.CharField(max_length=25)
    account_number=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.branch_name

# Create your models here.
