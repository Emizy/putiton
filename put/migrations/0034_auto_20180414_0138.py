# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-14 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('put', '0033_auto_20180413_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('Bags', 'Bags'), ('Clothing', 'Clothing'), ('Shoes', 'Shoes'), ('WeddingWears', 'WeddingWears'), ('Beads', 'Beads'), ('MakeupArtist', 'MakeupArtist'), ('Jewelry', 'Jewelry'), ('Hairstylist', 'Hairstylist'), ('Watches', 'Watches')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='moderate',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Yes', 'Yes')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supp_ads',
            name='category',
            field=models.CharField(blank=True, choices=[('beads', 'beads'), ('men_acc', 'men_acc'), ('men', 'men'), ('makeup', 'makeup'), ('women', 'women')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='confirm',
            field=models.CharField(blank=True, choices=[('UNAPPROVED', 'UNAPPROVED'), ('Nil', 'Nil'), ('APPROVED', 'APPROVED')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='status',
            field=models.CharField(blank=True, choices=[('Platinum', 'Platinum'), ('Gold', 'Gold'), ('Silver', 'Silver'), ('Free', 'Free'), ('NoSub', 'NoSub')], max_length=20, null=True),
        ),
    ]
