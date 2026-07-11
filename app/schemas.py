from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=5, max_length=255)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)