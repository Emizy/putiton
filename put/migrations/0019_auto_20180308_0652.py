# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-08 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('put', '0018_auto_20180308_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('Bags', 'Bags'), ('Beads', 'Beads'), ('Clothing', 'Clothing'), ('MakeupArtist', 'MakeupArtist'), ('Hairstylist', 'Hairstylist'), ('Shoes', 'Shoes'), ('Watches', 'Watches'), ('WeddingWears', 'WeddingWears'), ('Jewelry', 'Jewelry')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supp_ads',
            name='category',
            field=models.CharField(blank=True, choices=[('men', 'men'), ('men_acc', 'men_acc'), ('women', 'women'), ('makeup', 'makeup'), ('beads', 'beads')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='status',
            field=models.CharField(blank=True, choices=[('Platinum', 'Platinum'), ('Gold', 'Gold'), ('Silver', 'Silver'), ('Free', 'Free')], max_length=20, null=True),
        ),
    ]
