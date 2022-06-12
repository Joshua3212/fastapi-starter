from pydantic import BaseModel


class CreateItem(BaseModel):
    name: str
    description: str
