# Generated by Django 2.1.7 on 2019-03-30 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpiweb', '0002_auto_20190324_0332'),
    ]

    operations = [
        migrations.AddField(
            model_name='constraints',
            name='ConstraintDescr',
            field=models.TextField(null=True, verbose_name='Constraint Description'),
        ),
    ]