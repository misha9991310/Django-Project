from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.products.entities.products import Product as ProductEntity


class Product(TimedBaseModel):
    title = models.CharField(
        verbose_name='Название товара',
        max_length=255,
    )
    description = models.TextField(
        verbose_name='Описание товара',
        blank=True,
    )
    is_visible = models.BooleanField(
        verbose_name='Виден ли товар',
        default=True,
    )

    def __str__(self) -> str:
        return self.title

    def to_entity(self) -> ProductEntity:
        return ProductEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
