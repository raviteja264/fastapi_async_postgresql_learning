from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserResponse


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user_create: UserCreate) -> UserResponse:
        new_user = User(name=user_create.name, email=user_create.email)
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return UserResponse.model_validate(new_user)

    async def get_user_by_id(self, user_id: int) -> UserResponse | None:
        result = await self.db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            return UserResponse.model_validate(user)
        return None

    async def get_user_by_email(self, email: str) -> UserResponse | None:
        result = await self.db.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()
        if user:
            return UserResponse.model_validate(user)
        return None

    async def get_all_users(self) -> list[UserResponse]:
        result = await self.db.execute(select(User))
        users = result.scalars().all()
        return [UserResponse.model_validate(user) for user in users]
