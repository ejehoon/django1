# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Basket2(models.Model):
    firebase_uid = models.CharField(unique=True, max_length=255)
    product_id = models.CharField(max_length=255)
    product_title = models.CharField(db_column='Product_Title', max_length=1024)  # Field name made lowercase.
    product_per_price = models.CharField(db_column='Product_Per_Price', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basket2'
