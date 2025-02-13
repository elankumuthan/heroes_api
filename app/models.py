from sqlmodel import SQLModel, Field

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_power: str | None = Field(default=None)
    gender: str | None = Field(default=None)
    real_name: str | None = Field(default=None)
