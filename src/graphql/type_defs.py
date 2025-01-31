import graphene
from src.graphql.resolvers import AssignMemberMutation, GetCardMembersQuery

class Query(graphene.ObjectType):
    get_card_members = GetCardMembersQuery.Field()

class Mutation(graphene.ObjectType):
    assign_member = AssignMemberMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
