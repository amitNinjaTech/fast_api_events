from pydantic import BaseModel

class APIBase(BaseModel):
    name: str
    path: str

class API(APIBase):
    id: int

    class Config:
        orm_mode = True
