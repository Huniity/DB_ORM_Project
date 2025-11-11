from src.models.user import User
from src.settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(
        self,
        driver=settings.database_driver,
        host=settings.database_host,
        name=settings.database_name,
        password=settings.database_password,
        port=settings.database_port,
        username=settings.database_username,
    ):
        self.engine = create_engine(
            f"{driver}://{username}:{password}@{host}:{port}/{name}"
        )
        self.Session = sessionmaker(bind=self.engine)

    def create_user(self, name: str, email: str) -> User:
        user = User(name=name, email=email)

        with self.Session() as session:
            session.add(user)
            session.commit()

        return session.query(User).filter(User.email == email).first()

    def get_user(self, user_id: int) -> User | None:
        with self.Session() as session:
            return session.query(User).filter(User.id == user_id).first()

    def delete_user(self, id: int): ...
    def update_user(self, id: int, name: str, email: str): ...


if __name__ == "__main__":
    ...
