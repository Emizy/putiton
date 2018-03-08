# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-08 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('put', '0017_auto_20180307_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='offer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('ClothingAccessories', 'ClothingAccessories'), ('Jewelry', 'Jewelry'), ('Shoes', 'Shoes'), ('Bags', 'Bags'), ('Beads', 'Beads'), ('MakeupArtist', 'MakeupArtist'), ('Clothing', 'Clothing'), ('Watches', 'Watches'), ('WeddingWears', 'WeddingWears'), ('Hairstylist', 'Hairstylist')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supp_ads',
            name='category',
            field=models.CharField(blank=True, choices=[('men_acc', 'men_acc'), ('women', 'women'), ('makeup', 'makeup'), ('beads', 'beads'), ('men', 'men')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='status',
            field=models.CharField(blank=True, choices=[('Gold', 'Gold'), ('Platinum', 'Platinum'), ('Silver', 'Silver'), ('Free', 'Free')], max_length=20, null=True),
        ),
    ]