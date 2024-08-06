from pydantic import BaseModel, Field

from typing import Any, Generic, TypeVar

from ninja import Schema

from core.api.filtres import PaginationOut

TData = TypeVar("TData")
TListItem = TypeVar("TlistItem")


class PingResponseSchema(Schema):
    resalt: bool



class ListPaginatedResponse(Schema, Generic[TListItem]):
    items: list[TListItem]
    pagination: PaginationOut


class ApiResponse(Schema, Generic[TData]):
    data: TData | dict = Field(default_factory=dict)
    meta: dict[str, Any] = Field(default_factory=dict)
    errors: list[Any] = Field(default_factory=list)


