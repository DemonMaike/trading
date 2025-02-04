from enum import Enum
from fastapi import Depends, FastAPI
from typing import List, Optional
import fastapi_users
from fastapi_users.fastapi_users import FastAPIUsers
from pydantic import BaseModel
from pydantic.fields import Field
from datetime import datetime
from src.auth.auth import auth_backend
from src.auth.manager import get_user_manager
from src.auth.schemas import User, UserCreate, UserRead

app = FastAPI(
    title="Trading App"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


@app.get('/protected-route')
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"
