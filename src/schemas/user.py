from pydantic import BaseModel


class CreateUserPayload(BaseModel):
    name: str
    email: str
