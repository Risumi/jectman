# Generated by Django 2.1.7 on 2019-09-10 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jectman', '0003_auto_20190910_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backlog',
            name='begindate',
        ),
        migrations.RemoveField(
            model_name='backlog',
            name='enddate',
        ),
        migrations.RemoveField(
            model_name='project',
            name='issprinting',
        ),
        migrations.AddField(
            model_name='backlog',
            name='assignee',
            field=models.ForeignKey(blank=True, db_column='Assignee', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assignee', to='jectman.User'),
        ),
        migrations.AddField(
            model_name='backlog',
            name='createdby',
            field=models.ForeignKey(blank=True, db_column='CreatedBy', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='createdbyb', to='jectman.User'),
        ),
        migrations.AddField(
            model_name='backlog',
            name='createddate',
            field=models.DateField(blank=True, db_column='CreatedDate', null=True),
        ),
        migrations.AddField(
            model_name='backlog',
            name='id_epic',
            field=models.ForeignKey(blank=True, db_column='ID_Epic', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jectman.Epic'),
        ),
        migrations.AddField(
            model_name='backlog',
            name='id_project',
            field=models.ForeignKey(blank=True, db_column='ID_Project', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jectman.Project'),
        ),
        migrations.AddField(
            model_name='backlog',
            name='id_sprint',
            field=models.ForeignKey(blank=True, db_column='ID_Sprint', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jectman.Sprint'),
        ),
        migrations.AddField(
            model_name='backlog',
            name='modifiedby',
            field=models.ForeignKey(blank=True, db_column='ModifiedBy', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modifiedbyb', to='jectman.User'),
        ),
        migrations.AddField(
            model_name='backlog',
            name='modifieddate',
            field=models.DateField(blank=True, db_column='ModifiedDate', null=True),
        ),
        migrations.AddField(
            model_name='epic',
            name='createdby',
            field=models.ForeignKey(blank=True, db_column='CreatedBy', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='createdbye', to='jectman.User'),
        ),
        migrations.AddField(
            model_name='epic',
            name='id_project',
            field=models.ForeignKey(blank=True, db_column='ID_Project', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jectman.Project'),
        ),
        migrations.AddField(
            model_name='epic',
            name='modifiedby',
            field=models.ForeignKey(blank=True, db_column='ModifiedBy', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modifiedbye', to='jectman.User'),
        ),
        migrations.AddField(
            model_name='project',
            name='id_user',
            field=models.ForeignKey(blank=True, db_column='ID_User', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jectman.User'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(blank=True, db_column='Status', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='sprint',
            name='createdby',
            field=models.ForeignKey(blank=True, db_column='CreatedBy', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='createdbys', to='jectman.User'),
        ),
        migrations.AddField(
            model_name='sprint',
            name='createddate',
            field=models.DateField(blank=True, db_column='CreatedDate', null=True),
        ),
        migrations.AddField(
            model_name='sprint',
            name='id_project',
            field=models.ForeignKey(blank=True, db_column='ID_Project', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jectman.Project'),
        ),
        migrations.AddField(
            model_name='sprint',
            name='modifiedby',
            field=models.ForeignKey(blank=True, db_column='ModifiedBy', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='modifiedbys', to='jectman.User'),
        ),
        migrations.AddField(
            model_name='sprint',
            name='modifieddate',
            field=models.DateField(blank=True, db_column='ModifiedDate', null=True),
        ),
        migrations.AddField(
            model_name='sprint',
            name='name',
            field=models.CharField(blank=True, db_column='Name', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sprint',
            name='retrospective',
            field=models.TextField(blank=True, db_column='Retrospective', null=True),
        ),
        migrations.AddField(
            model_name='sprint',
            name='status',
            field=models.CharField(blank=True, db_column='Status', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='sprintreport',
            name='id_sprint',
            field=models.ForeignKey(blank=True, db_column='ID_Sprint', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jectman.Sprint'),
        ),
        migrations.AddField(
            model_name='userproject',
            name='email',
            field=models.ForeignKey(blank=True, db_column='Email', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jectman.User'),
        ),
        migrations.AddField(
            model_name='userproject',
            name='id_project',
            field=models.ForeignKey(blank=True, db_column='ID_Project', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jectman.Project'),
        ),
    ]