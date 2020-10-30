from dataclasses import dataclass
from pydantic import BaseModel, constr


@dataclass
class User:
    id: int
    name: str
    email: str
    password: str


class CreateUserDto(BaseModel):
    name: constr(max_length=50)
    email: constr(max_length=100, regex=r"[\w.]+@\w+\.[a-zA-Z0-9]+$")
    password: constr(
        max_length=12,
        min_length=6,
        regex=r"^(?=.*[0-9])(?=.*[a-z])(?=.*[@$#&_])(?=.*[A-Z])([\w@$#&_]+)$",
    )


class LoginUserDto(BaseModel):
    email: str
    password: str
