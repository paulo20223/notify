from typing import Optional
from pydantic import BaseModel


class Reservation(BaseModel):
    name: str
    telegram: Optional[str]
    email: str
    time: str
