# Generated by Django 2.1.1 on 2019-02-18 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_auto_20190218_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackingform',
            name='month_year',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='trackingform',
            name='supervisor',
            field=models.CharField(choices=[('C', 'Celena'), ('H', 'Heidi'), ('G', 'Gail'), ('K', 'Katie'), ('P', 'Pete'), ('M', 'Melanie'), ('N', 'Nicole')], max_length=1),
        ),
    ]