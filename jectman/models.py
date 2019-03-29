# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Backlog(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=8)  # Field name made lowercase.
    id_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='ID_Project', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    begindate = models.DateField(db_column='BeginDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Backlog'


class Project(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=8)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Project'
