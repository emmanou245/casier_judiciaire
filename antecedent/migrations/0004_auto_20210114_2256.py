# Generated by Django 3.1.3 on 2021-01-14 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antecedent', '0003_auto_20210114_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedent',
            name='date_des_faits',
            field=models.DateTimeField(null=True),
        ),
    ]
