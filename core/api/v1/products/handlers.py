from django.http import HttpRequest
from ninja import Router

from core.api.v1.products.schamas import ProductsListSchema

router = Router(tags=['Products'])


@router.get('', response=ProductsListSchema)
def get_product_list_handler(request: HttpRequest) -> ProductsListSchema:
    return []