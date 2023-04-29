from typing import Optional
from pydantic import BaseModel


class Message(BaseModel):
    name: str
    email: str
    telegram: Optional[str]
    website: Optional[str]
    date: str

    @property
    def display_message(self):
        message = f"Name: {self.name}\n" \
                  f"Email: {self.email}\n" \
                  f"Date: {self.date}\n"

        if self.telegram:
            message += f"Telegram: {self.telegram}\n"

        if self.telegram:
            message += f"Website: {self.website}\n"

        return message
