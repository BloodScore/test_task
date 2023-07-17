from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Manufacturer(BaseModel):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'manufacturers'


class Contract(BaseModel):
    class Meta:
        db_table = 'contracts'


class CreditRequest(BaseModel):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, primary_key=True, related_name='credit_request')

    class Meta:
        db_table = 'credit_requests'


class Product(BaseModel):
    name = models.CharField(max_length=64)

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    credit_request = models.ForeignKey(CreditRequest, on_delete=models.CASCADE, related_name='products')

    class Meta:
        db_table = 'products'
