from sqlalchemy.exc import IntegrityError
from fastapi import FastAPI, Response, HTTPException, status
import json

from src.database import Database
from src.schemas.user import CreateUserPayload

app = FastAPI()
database = Database()


@app.post("/users")
def post_user(payload: CreateUserPayload):
    try:
        user = database.create_user(email=payload.email, name=payload.name)

        return Response(
            content=json.dumps({"user_id": user.id}),
            status_code=status.HTTP_201_CREATED,
        )

    except IntegrityError:
        raise HTTPException(
            detail="Something went wrong", status_code=status.HTTP_400_BAD_REQUEST
        )

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = database.get_user(user_id=user_id)

    if not user:
        raise HTTPException(
            detail="User not found", status_code=status.HTTP_404_NOT_FOUND
        )

    return {"id": user.id, "name": user.name, "email": user.email}




