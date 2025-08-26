from beanie import Document
from pydantic import BaseModel, Field # modelar as classes
from datetime import datetime
from typing import List

#validação de payload (POST/PUT/PATCH)

class ProductIn(BaseModel):
    name: str = Field(min_length=2)
    price: float = Field(ge=0)


class Product(Document, ProductIn):
    Created_at: datetime = Field(default_factory=datetime.utcnow)


