from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserResponse


class UserService:
    def __init__(self, db: AsyncSession):
        self.user_repository = UserRepository(db)

    async def create_user(self, user_create: UserCreate) -> UserResponse:
        return await self.user_repository.create_user(user_create)

    async def get_user_by_id(self, user_id: int) -> UserResponse | None:
        return await self.user_repository.get_user_by_id(user_id)

    async def get_user_by_email(self, email: str) -> UserResponse | None:
        return await self.user_repository.get_user_by_email(email)

    async def get_all_users(self) -> list[UserResponse]:
        return await self.user_repository.get_all_users()
