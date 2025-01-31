from pydantic import BaseModel, validator

class AssignMemberSchema(BaseModel):
    card_id: int
    user_id: int

    @validator("card_id", "user_id")
    def must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("El ID debe ser un número positivo.")
        return v
