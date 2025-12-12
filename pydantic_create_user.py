import uuid
from pydantic import BaseModel, Field, EmailStr, constr
from tools.fakers import fake

class UserSchema(BaseModel):
    """
    Структура описания пользователя
    """
    id: str
    email: EmailStr = Field(default_factory= lambda: fake.email())
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName",default="Mike")
    middle_name: str = Field(alias="middleName",default="Test")

class CreateUserRequestSchema(BaseModel):
    """
    Структура описания запроса создания пользователя
    """
    email: EmailStr = Field(default_factory= lambda: fake.email())
    password: constr(min_length=6)
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName",default="Mike")
    middle_name: str = Field(alias="middleName",default="Test")

class CreateUserResponseSchema(BaseModel):
    """
    Структура описания ответа на запрос создания пользователя
    """
    user: UserSchema

