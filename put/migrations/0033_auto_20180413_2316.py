# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-13 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('put', '0032_auto_20180413_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='store_visit',
        ),
        migrations.AddField(
            model_name='supplier',
            name='store_visit',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, choices=[('Bags', 'Bags'), ('Clothing', 'Clothing'), ('Hairstylist', 'Hairstylist'), ('Beads', 'Beads'), ('Shoes', 'Shoes'), ('WeddingWears', 'WeddingWears'), ('Jewelry', 'Jewelry'), ('MakeupArtist', 'MakeupArtist'), ('Watches', 'Watches')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='moderate',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supp_ads',
            name='category',
            field=models.CharField(blank=True, choices=[('beads', 'beads'), ('women', 'women'), ('men', 'men'), ('makeup', 'makeup'), ('men_acc', 'men_acc')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='confirm',
            field=models.CharField(blank=True, choices=[('APPROVED', 'APPROVED'), ('Nil', 'Nil'), ('UNAPPROVED', 'UNAPPROVED')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='status',
            field=models.CharField(blank=True, choices=[('Free', 'Free'), ('Gold', 'Gold'), ('Silver', 'Silver'), ('NoSub', 'NoSub'), ('Platinum', 'Platinum')], max_length=20, null=True),
        ),
    ]
