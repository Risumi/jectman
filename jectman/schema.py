import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Project, Backlog, Sprint
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
    id_project = graphene.String()    
    begindate = graphene.Date()
    enddate = graphene.Date()
    goal = graphene.String()
    #2
    class Arguments:
        id = graphene.String()
        id_project = graphene.String()    
        begindate = graphene.Date()
        enddate = graphene.Date()
        goal = graphene.String() 

    #3
    def mutate(self, info, id, id_project,begindate,enddate,goal):
        project = Project(id=id_project)
        sprint = Sprint(id=id, id_project=project,begindate=begindate,enddate=enddate,goal=goal)
        sprint.save()

        return CreateSprint(
            id = sprint.id,
            id_project = project.id,
            begindate = sprint.begindate,
            enddate = sprint.enddate,
            goal = sprint.goal             
        )

class CreateBacklogSprint(graphene.Mutation):
    id = graphene.String()
    id_project = graphene.String()
    id_sprint = graphene.String()
    name = graphene.String()        
    status = graphene.String()
    begindate = graphene.Date()
    enddate = graphene.Date()
    description = graphene.String()
    #2
    class Arguments:
        id = graphene.String()
        id_project = graphene.String()
        id_sprint = graphene.String() 
        name = graphene.String()        
        status = graphene.String()
        begindate = graphene.Date()
        enddate = graphene.Date()
        description = graphene.String()

    #3
    def mutate(self, info, id,id_project,id_sprint,name,status,begindate,enddate,description):
        project = Project(id=id_project)
        sprint = Sprint(id=id_sprint)
        backlog = Backlog(id=id,id_project=project,id_sprint=id_sprint,name=name,status=status,begindate=begindate,enddate=enddate,description=description)        
        backlog.save()
        return CreateBacklog(
            id = backlog.id,
            id_project = project.id,
            id_sprint = sprint.id,
            name = backlog.name,
            status = backlog.status,
            begindate = backlog.begindate,
            enddate = backlog.enddate,
            description = backlog.description
        )

class CreateBacklog(graphene.Mutation):
    id = graphene.String()
    id_project = graphene.String()    
    name = graphene.String()        
    status = graphene.String()
    begindate = graphene.Date()
    enddate = graphene.Date()
    description = graphene.String()
    #2
    class Arguments:
        id = graphene.String()
        id_project = graphene.String()        
        name = graphene.String()        
        status = graphene.String()
        begindate = graphene.Date()
        enddate = graphene.Date()
        description = graphene.String()

    #3
    def mutate(self, info, id,id_project,name,status,begindate,enddate,description):
        project = Project(id=id_project)        
        backlog = Backlog(id=id,id_project=project,name=name,status=status,begindate=begindate,enddate=enddate,description=description)        
        backlog.save()
        return CreateBacklog(
            id = backlog.id,
            id_project = project.id,            
            name = backlog.name,
            status = backlog.status,
            begindate = backlog.begindate,
            enddate = backlog.enddate,
            description = backlog.description
        )
#4
class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()
    create_backlog = CreateBacklog.Field()
    create_backlogsprint = CreateBacklogSprint.Field()
    create_sprint = CreateSprint.Field()

class Query(object):
    all_project= graphene.List(ProjectType)    
    backlog = graphene.List(BacklogType, id=graphene.String())
    sprint = graphene.List(SprintType, id=graphene.String())
    
    def resolve_all_project(self, info, **kwargs):
        return Project.objects.all()

    def resolve_backlog(self, info, id=None, **kwargs):
            # The value sent with the search parameter will be in the args variable         
            if id:
                filter = (
                    Q(id_project__id__iexact=id)                    
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

# class CustomNode(relay.Node): 
#     class Meta:
#         name = 'Node'

#     @staticmethod
#     def to_global_id(type, id):
#         #returns a non-encoded ID
#         return id

#     @staticmethod
#     def get_node_from_global_id(info, global_id, only_type=None):
#         model = getattr(Query,info.field_name).field_type._meta.model
#         return model.objects.get(id=global_id)

# class BacklogNode(DjangoObjectType):
#     class Meta:
#         # Assume you have an Animal model defined with the following fields
#         model = Backlog
#         filter_fields = ['id_project']
#         interfaces = (CustomNode,)        