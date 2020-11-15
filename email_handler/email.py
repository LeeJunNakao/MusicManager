from pydantic import BaseModel
from typing import Optional


class EmailDto(BaseModel):
    receiver: str
    message: str
    subject: Optional[str]
