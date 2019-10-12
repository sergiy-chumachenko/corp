import graphene
from graphene_django import DjangoObjectType
from company.models import JobTitle, City, Employee
from graphene_django.filter import DjangoFilterConnectionField


class CityNode(DjangoObjectType):
    class Meta:
        model = City
        filter_fields = ['name']
        interfaces = (graphene.relay.Node,)


class JobTitleNode(DjangoObjectType):
    class Meta:
        model = JobTitle
        filter_fields = ['name']
        interfaces = (graphene.relay.Node,)


class EmployeeNode(DjangoObjectType):
    class Meta:
        model = Employee
        filter_fields = (
            'first_name',
            'last_name',
            'job_title__name',
            'city__name',
        )
        interfaces = (graphene.relay.Node,)


class Query(object):
    city = graphene.relay.Node.Field(CityNode)
    all_cities = DjangoFilterConnectionField(CityNode)

    job_title = graphene.relay.Node.Field(JobTitleNode)
    all_job_titles = DjangoFilterConnectionField(JobTitleNode)

    employee = graphene.relay.Node.Field(EmployeeNode)
    all_employees = DjangoFilterConnectionField(EmployeeNode)
