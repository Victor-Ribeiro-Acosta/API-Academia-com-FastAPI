from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from fastapi import Depends
from config.database import get_session

DB_dependecy = Annotated[AsyncSession, Depends(get_session)]