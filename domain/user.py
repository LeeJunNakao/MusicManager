from dataclasses import dataclass
from pydantic import BaseModel, constr


@dataclass
class User:
    id: int
    name: str
    email: str
    password: str


@dataclass(frozen=True)
class UserDto(BaseModel):
    id: int
    name: constr(max_length=50)
    email: constr(max_length=100, regex=r"[\w|.]+@\w+\.[a-zA-Z0-9]+")
    password: constr(
        max_length=100,
        regex=r"^(?=.*[0-9])(?=.*[a-z])(?=.*[@$#&_])(?=.*[A-Z])([\w@$#&_]+)$",
    )
