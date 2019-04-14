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

class CustomNode(relay.Node): 
    class Meta:
        name = 'Node'

    @staticmethod
    def to_global_id(type, id):
        #returns a non-encoded ID
        return id

    @staticmethod
    def get_node_from_global_id(info, global_id, only_type=None):
        model = getattr(Query,info.field_name).field_type._meta.model
        return model.objects.get(id=global_id)

class BacklogNode(DjangoObjectType):
    class Meta:
        # Assume you have an Animal model defined with the following fields
        model = Backlog
        filter_fields = ['id_project']
        interfaces = (CustomNode,)        

class CreateProject(graphene.Mutation):
    id = graphene.String()
    name = graphene.String()    

    #2
    class Arguments:
        id = graphene.String()
        name = graphene.String()    

    #3
    def mutate(self, info, id, name):
        project = Project(id=id, name=name)
        project.save()

        return CreateLink(
            id=project.id,
            name=project.name,            
        )

#4
class Mutation(graphene.ObjectType):
    create_project = CreateProject.Field()

class Query(object):
    all_project= graphene.List(ProjectType)
    # all_backlog = graphene.List(BacklogType)
    backlog = graphene.List(BacklogType, id=graphene.String())
    sprint = graphene.List(SprintType, id=graphene.String())


    backloga = CustomNode.Field(BacklogNode)
    filter_backloga = DjangoFilterConnectionField(BacklogNode)

    def resolve_backlog(self, info, id=None, **kwargs):
            # The value sent with the search parameter will be in the args variable         
            if id:
                filter = (
                    Q(id_project__id__iexact=id)                    
                )
                return Backlog.objects.filter(filter)
            return Backlog.objects.all()

    def resolve_all_project(self, info, **kwargs):
        return Project.objects.all()

    def resolve_sprint(self, info, id=None, **kwargs):
            # The value sent with the search parameter will be in the args variable         
            if id:
                filter = (
                    Q(id_project__id__iexact=id)                    
                )
                return Sprint.objects.filter(filter)
            return Sprint.objects.all()

    # def resolve_all_backlog(self, info, **kwargs):
    #     # We can easily optimize query count in the resolve method
    #     return Backlog.objects.all()        
    
