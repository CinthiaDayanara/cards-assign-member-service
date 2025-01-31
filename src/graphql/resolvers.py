import graphene
from src.services.assignment_service import assign_member_to_card
from src.utils.validators import AssignMemberSchema

class AssignMemberMutation(graphene.Mutation):
    class Arguments:
        card_id = graphene.Int(required=True)
        user_id = graphene.Int(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    async def mutate(self, info, card_id, user_id):
        try:
            AssignMemberSchema(card_id=card_id, user_id=user_id)  # Validar entrada
            await assign_member_to_card(card_id, user_id)
            return AssignMemberMutation(success=True, message="Miembro asignado con éxito.")
        except Exception as e:
            return AssignMemberMutation(success=False, message=str(e))

class GetCardMembersQuery(graphene.ObjectType):
    card_id = graphene.Int(required=True)

    async def resolve_get_card_members(self, info, card_id):
        async with SessionLocal() as session:
            result = await session.execute(select(Member).where(Member.card_id == card_id))
            return [{"user_id": member.user_id} for member in result.scalars()]
