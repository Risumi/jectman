import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Project, Backlog, Sprint,User,Epic
from graphql_relay.node.node import from_global_id
from django.db.models import Q

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project


class BacklogType(DjangoObjectType):
    class Meta:
        model = Backlog

class SprintType(DjangoObjectType):
    class Meta:
        model = Sprint

class UserType(DjangoObjectType):
    class Meta:
        model = User

class EpicType(DjangoObjectType):
    class Meta:
        model = Epic


class ProgressType(graphene.ObjectType):
    id = graphene.String()
    complete = graphene.Int()
    count = graphene.Int()

class CreateProject(graphene.Mutation):
    id = graphene.String()
    name = graphene.String()    
    description = graphene.String()
    status = graphene.String()
    #2
    class Arguments:
        id = graphene.String()
        name = graphene.String()
        description = graphene.String()
        status = graphene.String()    

    #3
    def mutate(self, info, id, name,description,status):
        project = Project(id=id, name=name,description=description,status=status)
        project.save()

        return CreateProject(
            id=project.id,
            name=project.name,
            description=project.description,
            status=project.status            
        )
class CreateSprint(graphene.Mutation):
    id = graphene.String()
    name = graphene.String()
    id_project = graphene.String()    
    goal = graphene.String()
    createddate = graphene.Date()
    createdby = graphene.String()
    #2
    class Arguments:
        id = graphene.String()
        name = graphene.String()
        id_project = graphene.String()    
        goal = graphene.String()
        createddate = graphene.Date()
        createdby = graphene.String()

    #3
    def mutate(self, info, id,name, id_project,goal,createddate,createdby):
        project = Project(id=id_project)
        createby = User(email=createdby) 
        sprint = Sprint(id=id,name=name, id_project=project,goal=goal,createddate=createddate,createdby=createby)
        sprint.save()

        return CreateSprint(
            id = sprint.id,
            name = sprint.name,
            id_project = project.id,            
            goal = sprint.goal,
            createddate = sprint.createddate,
            createdby  = createby.email                               
        )

class EditSprint(graphene.Mutation):
    id = graphene.String()    
    name = graphene.String()
    begindate = graphene.Date()
    enddate = graphene.Date()
    goal = graphene.String()
    modifieddate = graphene.Date()
    modifiedby = graphene.String()
    #2
    class Arguments:
        id = graphene.String()    
        name = graphene.String()
        begindate = graphene.Date()
        enddate = graphene.Date()
        goal = graphene.String()
        modifieddate = graphene.Date()
        modifiedby = graphene.String() 

    #3
    def mutate(self, info, id,name,begindate,enddate,goal,modifieddate,modifiedby):        
        modifby = User(email=modifiedby)        
        sprint = Sprint(id=id,name=name,begindate=begindate,enddate=enddate,goal=goal,modifieddate=modifieddate,modifiedby=modifby)
        Sprint.objects.filter(id=id).update(name=name,begindate=begindate,enddate=enddate,goal=goal,modifieddate=modifieddate,modifiedby=modifby)                

        return EditSprint(
            id = sprint.id,            
            name = sprint.name,
            begindate = sprint.begindate,
            enddate = sprint.enddate,
            goal = sprint.goal,
            modifieddate = sprint.modifieddate,
            modifiedby = modifby.email            
        )

class CreateBacklog(graphene.Mutation):
    id = graphene.String()
    id_project = graphene.String()    
    id_epic = graphene.String()
    assignee = graphene.String()
    name = graphene.String()        
    status = graphene.String()
    description = graphene.String()
    createddate = graphene.Date()
    createdby = graphene.String()
    
    #2
    class Arguments:
        id = graphene.String()
        id_project = graphene.String()    
        id_epic = graphene.String()
        assignee = graphene.String()
        name = graphene.String()        
        status = graphene.String()
        description = graphene.String()
        createddate = graphene.Date()
        createdby = graphene.String()

    #3
    def mutate(self, info, id,id_project,id_epic,assignee,name,status,description,createddate,createdby):
        project = Project(id=id_project) 

        if assignee == "":
            assigne = None
        else :
            assigne = User(email=assignee)

        if id_epic == "":
            epic = None
        else :
            epic = Epic(id=id_epic)

        createby = User(email=createdby)        
        backlog = Backlog(id=id,id_project=project,id_epic=epic,assignee=assigne,name=name,status=status,description=description,createddate=createddate,createdby=createby)        
        backlog.save()
        return CreateBacklog(
            id = backlog.id,
            id_project = project.id,  
            # id_epic = epic.id,
            # assignee =assigne.email,
            name = backlog.name,
            status = backlog.status,
            description = backlog.description,
            createddate = backlog.createddate,
            createdby = assigne.email
        )

class EditBacklog(graphene.Mutation):
    id = graphene.String()
    id_epic = graphene.String()
    id_sprint = graphene.String()
    assignee = graphene.String()
    name = graphene.String()        
    status = graphene.String()
    description = graphene.String()
    modifieddate = graphene.Date()
    modifiedby = graphene.String()
    
    #2
    class Arguments:
        id = graphene.String()
        id_epic = graphene.String()
        id_sprint = graphene.String()
        assignee = graphene.String()
        name = graphene.String()        
        status = graphene.String()
        description = graphene.String()
        modifieddate = graphene.Date()
        modifiedby = graphene.String()

    #3
    def mutate(self, info, id,id_sprint,id_epic,assignee,name,status,description,modifieddate,modifiedby):           
        
        if assignee == "":
            assigne = None
        else :
            assigne = User(email=assignee)

        if id_epic == "":
            epic = None
        else :
            epic = Epic(id=id_epic)

        if id_sprint =="":
            sprint = None
        else :
            sprint = Sprint(id=id_sprint)

        modifby = User(email=modifiedby)        
        backlog = Backlog(id=id,id_epic=epic,id_sprint=sprint,assignee=assigne,name=name,status=status,description=description,modifieddate=modifieddate,modifiedby=modifby)       
        
        Backlog.objects.filter(id=id).update(id_epic=epic,id_sprint=sprint,assignee=assigne,name=name,status=status,description=description,modifieddate=modifieddate,modifiedby=modifby)        
    
        # backlog.save()
        return EditBacklog(
            id = backlog.id,             
            # id_epic = epic.id,
            # assignee =assigne.email,
            name = backlog.name,
            status = backlog.status,
            description = backlog.description,
            modifieddate = backlog.modifieddate,
            modifiedby = assigne.email
        )

class CreateUser(graphene.Mutation):
    email = graphene.String()
    nama = graphene.String()    
    password = graphene.String()            
    #2
    class Arguments:
        email = graphene.String()
        nama = graphene.String()    
        password = graphene.String()                

    #3
    def mutate(self, info, email,nama,password):        
        user = User(email=email,nama=nama,password=password)        
        user.save()
        return CreateUser(
            email = user.email,
            nama = user.nama,            
            password = user.password
        )

class CreateEpic(graphene.Mutation):
    id = graphene.String()
    id_project = graphene.String()    
    name = graphene.String()            
    summary = graphene.String()            
    createddate = graphene.Date()            
    createdby = graphene.String()            
    #2
    class Arguments:
        id = graphene.String()
        id_project = graphene.String()    
        name = graphene.String()            
        summary = graphene.String()            
        createddate = graphene.Date()            
        createdby = graphene.String()   
    #3
    def mutate(self, info, id,id_project,name,summary,createddate,createdby):        
        project = Project(id=id_project)
        createby= User(email=createdby)
        epic = Epic(id=id,id_project=project,name=name,summary=summary,createddate=createddate,createdby=createby)  
        epic.save()
        return CreateEpic(
            id = epic.id,
            id_project = project.id,
            name = epic.name,
            summary = epic.summary,
            createddate = epic.createddate,
            createdby = createby.Email
        )

class EditEpic(graphene.Mutation):
    id = graphene.String()
    id_project = graphene.String()    
    name = graphene.String()            
    summary = graphene.String()            
    modifieddate = graphene.Date()            
    modifiedby = graphene.String()            
    #2
    class Arguments:
        id = graphene.String()
        id_project = graphene.String()    
        name = graphene.String()            
        summary = graphene.String()            
        modifieddate = graphene.Date()            
        modifiedby = graphene.String()   
    #3
    def mutate(self, info, id,id_project,name,summary,modifieddate,modifiedby):        
        project = Project(id=id_project)
        modifby= User(email=modifiedby)        
        epic = Epic(id=id,id_project=project,name=name,summary=summary,modifieddate=modifieddate,modifiedby=modifby)  
        Epic.objects.filter(id=id).update(id_project=project,name=name,summary=summary,modifieddate=modifieddate,modifiedby=modifby)          
        return EditEpic(
            id = epic.id,
            id_project = project.id,
            name = epic.name,
            summary = epic.summary,
            modifieddate = epic.modifieddate,
            modifiedby = modifby.Email
        )

class DeleteBacklog(graphene.Mutation):
    id = graphene.String()         
    #2
    class Arguments:
        id = graphene.String()
 
    #3
    def mutate(self, info, id):        
        backlog = Backlog(id=id)     
        test = id   
        backlog.delete()
        return DeleteBacklog(
            id = test,
        )

class DeleteEpic(graphene.Mutation):
    id = graphene.String()         
    #2
    class Arguments:
        id = graphene.String()
 
    #3
    def mutate(self, info, id):        
        epic = Epic(id=id)     
        test = id   
        epic.delete()
        return DeleteEpic(
            id = test,
        )


class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()
    create_backlog = CreateBacklog.Field()
    edit_backlog = EditBacklog.Field()    
    create_sprint = CreateSprint.Field()
    edit_sprint = EditSprint.Field()
    create_user = CreateUser.Field()
    create_epic = CreateEpic.Field()
    edit_epic = EditEpic.Field()
    delete_backlog = DeleteBacklog.Field()
    delete_epic = DeleteEpic.Field()

class Query(object):
    project= graphene.List(ProjectType)    
    backlog = graphene.List(BacklogType, id=graphene.String())
    backlogE=graphene.List(BacklogType,id_epic=graphene.String())
    sprint = graphene.List(SprintType, id=graphene.String())    
    epic = graphene.List(EpicType, id=graphene.String())
    user = graphene.List(UserType, email=graphene.String(), password=graphene.String())    
    progress = graphene.List(ProgressType)

    def resolve_progress(self, info, **kwargs):                
        id = Project.objects.values_list('id', flat=True)
        progress = []
        
        for i in id:      
            p = ProgressType()   
            p.id = i
            p.complete = Backlog.objects.filter(id_project__id__iexact=i,status__icontains='Completed').count()
            p.count = Backlog.objects.filter(id_project__id__iexact=i).count() 
            progress.append(p)
        # a = Progress
        # a.id ="a" 
        return progress
    
    def resolve_project(self, info, **kwargs):
        return Project.objects.all()

    def resolve_backlog(self, info, id=None, **kwargs):
            # The value sent with the search parameter will be in the args variable         
            if id:
                filter = (
                    Q(id_project__id__iexact=id )                   
                )
                return Backlog.objects.filter(filter)
            return Backlog.objects.all()    
    

    def resolve_backlogE(self, info, id_epic=None, **kwargs):
            # The value sent with the search parameter will be in the args variable         
            if id:
                filter = (
                    Q( id_epic__id__iexact = id_epic)                   
                )
                return Backlog.objects.filter(filter)
            return Backlog.objects.all()    

    def resolve_sprint(self, info, id=None, **kwargs):
            # The value sent with the search parameter will be in the args variable         
            if id:
                filter = (
                    Q(id_project__id__iexact=id)                    
                )
                return Sprint.objects.filter(filter)
            return Sprint.objects.all()       

    def resolve_epic(self, info, id=None, **kwargs):
            # The value sent with the search parameter will be in the args variable         
            if id:
                filter = (
                    Q(id_project__id__iexact=id)                    
                )
                return Epic.objects.filter(filter)
            return Epic.objects.all()  
            
    def resolve_user(self, info, email=None, password=None, **kwargs):
            # The value sent with the search parameter will be in the args variable         
            if id:
                filter = (
                    Q(email__exact=email,password__exact=password)                    
                )
                return User.objects.filter(filter)
            return User.objects.all()  