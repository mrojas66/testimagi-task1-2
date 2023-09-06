from fastapi import APIRouter
from models.users import UserCreate, User
from services.user_service import create_user, get_user_by_username

router = APIRouter()

@router.post("/", response_model=User)
def create_user_route(user: UserCreate):
    return create_user(user)

@router.get("/{user_id}", response_model=User)
def read_user_route(user_id: int):
    return get_user_by_username(user_id)
