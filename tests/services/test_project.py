import pytest

from core.api.filtres import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.services.products import BaseProductService
from tests.factories.products import ProductModelFactory


@pytest.mark.django_db
def test_products_count_zero(product_service: BaseProductService):
    product_count = product_service.get_product_count(ProductFilters())
    assert product_count == 0, f'{product_count=}'


@pytest.mark.django_db
def test_get_products_count_exist(product_service: BaseProductService):
    expected_count = 5
    ProductModelFactory.create_batch(size=expected_count)

    product_count = product_service.get_product_count(ProductFilters())
    assert product_count == expected_count , f'{product_count=}'


@pytest.mark.django_db
def test_get_products_all(product_service: BaseProductService):
    expected_count = 5
    products = ProductModelFactory.create_batch(size=expected_count)
    products_titles = {product.title for product in products}

    fetched_products = product_service.get_product_list(ProductFilters(), PaginationIn())
    fetched_titles = {product.title for product in fetched_products}

    assert len(fetched_titles) == expected_count, f'{fetched_titles=}'
    assert products_titles == fetched_titles, f'{products_titles}'
