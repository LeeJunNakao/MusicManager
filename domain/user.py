from typing import List, Optional
from dataclasses import dataclass
from pydantic import BaseModel, constr
from domain.music import Music


class User(BaseModel):
    class Config:
        orm_mode = True

    id: Optional[int]
    name: str
    email: str
    password: str
    musics: List[Music]


class CreateUserDto(BaseModel):
    name: constr(min_length=1, max_length=50)
    email: constr(max_length=100, regex=r"[\w.]+@\w+\.[a-zA-Z0-9]+$")
    password: constr(
        max_length=12,
        min_length=6,
        regex=r"^(?=.*[0-9])(?=.*[a-z])(?=.*[@$#&_])(?=.*[A-Z])([\w@$#&_]+)$",
    )


class LoginUserDto(BaseModel):
    email: constr(max_length=100, regex=r"[\w.]+@\w+\.[a-zA-Z0-9]+$")
    password: constr(
        max_length=12,
        min_length=6,
        regex=r"^(?=.*[0-9])(?=.*[a-z])(?=.*[@$#&_])(?=.*[A-Z])([\w@$#&_]+)$",
    )


class UpdateUserDto(BaseModel):
    id: int
    name: Optional[constr(max_length=50)]
    email: Optional[constr(max_length=100, regex=r"[\w.]+@\w+\.[a-zA-Z0-9]+$")]
    password: Optional[
        constr(
            max_length=12,
            min_length=6,
            regex=r"^(?=.*[0-9])(?=.*[a-z])(?=.*[@$#&_])(?=.*[A-Z])([\w@$#&_]+)$",
        )
    ]


class GetUserDto(BaseModel):
    id: int
    name: str
    email: str
