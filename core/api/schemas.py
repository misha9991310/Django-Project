from pydantic import BaseModel


class PingResponseSchema(BaseModel):
    resalt: bool