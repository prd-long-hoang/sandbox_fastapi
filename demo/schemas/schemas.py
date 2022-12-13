from pydantic import BaseModel


class FullDetailUser(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class SellPlacesBase(BaseModel):
    location_name: str
    street: str | None
    city: str | None
    state: str | None


class CreateSellPlaces(SellPlacesBase):
    pass
