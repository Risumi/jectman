# Generated by Django 2.1.7 on 2019-09-10 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jectman', '0004_auto_20190910_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backlog',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='backlog',
            name='createdby',
        ),
        migrations.RemoveField(
            model_name='backlog',
            name='id_epic',
        ),
        migrations.RemoveField(
            model_name='backlog',
            name='id_project',
        ),
        migrations.RemoveField(
            model_name='backlog',
            name='id_sprint',
        ),
        migrations.RemoveField(
            model_name='backlog',
            name='modifiedby',
        ),
        migrations.RemoveField(
            model_name='epic',
            name='createdby',
        ),
        migrations.RemoveField(
            model_name='epic',
            name='id_project',
        ),
        migrations.RemoveField(
            model_name='epic',
            name='modifiedby',
        ),
        migrations.RemoveField(
            model_name='project',
            name='id_user',
        ),
        migrations.RemoveField(
            model_name='sprint',
            name='createdby',
        ),
        migrations.RemoveField(
            model_name='sprint',
            name='id_project',
        ),
        migrations.RemoveField(
            model_name='sprint',
            name='modifiedby',
        ),
        migrations.RemoveField(
            model_name='sprintreport',
            name='id_sprint',
        ),
        migrations.RemoveField(
            model_name='userproject',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userproject',
            name='id_project',
        ),
        migrations.DeleteModel(
            name='Backlog',
        ),
        migrations.DeleteModel(
            name='Epic',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Sprint',
        ),
        migrations.DeleteModel(
            name='Sprintreport',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Userproject',
        ),
    ]