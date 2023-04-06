# Generated by Django 4.1.7 on 2023-04-06 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_column_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='status',
            field=models.IntegerField(choices=[(1, 'New'), (2, 'In Progress'), (3, 'In QA'), (4, 'Ready'), (5, 'Done')], default=1),
        ),
    ]
