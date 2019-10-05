# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    email = models.CharField(db_column='Email', primary_key=True, max_length=50)  # Field name made lowercase.
    nama = models.CharField(db_column='Nama', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'User'
        
class Project(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=8)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='ID_User', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Project'


class Epic(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    id_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='ID_Project', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    summary = models.TextField(db_column='Summary', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    createdby = models.ForeignKey('User', models.DO_NOTHING, db_column='CreatedBy', blank=True, null=True,related_name='createdbye')  # Field name made lowercase.
    modifiedby = models.ForeignKey('User', models.DO_NOTHING, db_column='ModifiedBy', blank=True, null=True,related_name='modifiedbye')  # Field name made lowercase.

    class Meta:
        db_table = 'Epic'



class Sprint(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=10)  # Field name made lowercase.
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='ID_Project', blank=True, null=True)  # Field name made lowercase.
    begindate = models.DateField(db_column='BeginDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    goal = models.TextField(db_column='Goal', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    createdby = models.ForeignKey('User', models.DO_NOTHING, db_column='CreatedBy', blank=True, null=True,related_name='createdbys')  # Field name made lowercase.
    modifiedby = models.ForeignKey('User', models.DO_NOTHING, db_column='ModifiedBy', blank=True, null=True,related_name='modifiedbys')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    retrospective = models.TextField(db_column='Retrospective', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Sprint'

class Backlog(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=8)  # Field name made lowercase.
    id_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='ID_Project', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    id_sprint = models.ForeignKey('Sprint', models.DO_NOTHING, db_column='ID_Sprint', blank=True, null=True)  # Field name made lowercase.
    assignee = models.ForeignKey('User', models.DO_NOTHING, db_column='Assignee', blank=True, null=True,related_name='assignee')  # Field name made lowercase.
    id_epic = models.ForeignKey('Epic', models.DO_NOTHING, db_column='ID_Epic', blank=True, null=True)  # Field name made lowercase.
    createdby = models.ForeignKey('User', models.DO_NOTHING, db_column='CreatedBy', blank=True, null=True,related_name='createdbyb')  # Field name made lowercase.
    modifiedby = models.ForeignKey('User', models.DO_NOTHING, db_column='ModifiedBy', blank=True, null=True,related_name='modifiedbyb')  # Field name made lowercase.

    class Meta:
        db_table = 'Backlog'


class BacklogSprint(models.Model):
    id_sprint = models.ForeignKey('Sprint', models.DO_NOTHING, db_column='ID_Sprint', blank=True, null=True)  # Field name made lowercase.
    id_backlog = models.ForeignKey('Backlog', models.DO_NOTHING, db_column='ID_Backlog', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'BacklogSprint'


class Userproject(models.Model):
    email = models.ForeignKey(User, models.DO_NOTHING, db_column='Email', blank=True, null=True)  # Field name made lowercase.
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='ID_Project', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'UserProject'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
