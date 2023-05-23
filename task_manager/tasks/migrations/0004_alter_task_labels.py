# Generated by Django 4.2.1 on 2023-05-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0003_tasklabels_task_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, through='tasks.TaskLabels', to='labels.label', verbose_name='Labels'),
        ),
    ]
