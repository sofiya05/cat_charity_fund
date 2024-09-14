from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):
    async def get_charity_project_id_by_name(
        self, charity_project_name: str, session: AsyncSession
    ) -> Optional[int]:
        db_charity_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charity_project_name
            )
        )
        return db_charity_project_id.scalars().first()

    async def get_charity_project_by_id(
        self, charity_project_id: str, session: AsyncSession
    ) -> Optional[CharityProject]:
        charity_project = await session.execute(
            select(CharityProject).where(
                CharityProject.id == charity_project_id
            )
        )
        return charity_project.scalars().first()


charity_project_crud = CRUDCharityProject(CharityProject)
