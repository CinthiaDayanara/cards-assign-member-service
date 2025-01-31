from sqlalchemy.future import select
from src.models.database import SessionLocal
from src.models.member import Member

async def assign_member_to_card(card_id: int, user_id: int):
    async with SessionLocal() as session:
        existing_assignment = await session.execute(
            select(Member).where(Member.card_id == card_id, Member.user_id == user_id)
        )
        if existing_assignment.scalar():
            raise ValueError("El usuario ya está asignado a esta tarjeta.")

        new_assignment = Member(card_id=card_id, user_id=user_id)
        session.add(new_assignment)
        await session.commit()
        return new_assignment
