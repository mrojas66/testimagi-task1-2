from models.users import UserCreate, User
from sqlalchemy.orm import Session
from entities.user_entity import UserEntity
db_users = []


def create_user(db: Session, user: UserCreate):
    db_user = UserEntity(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, username: str):
    return db.query(UserEntity).filter(UserEntity.username == username).first()
