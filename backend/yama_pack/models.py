from django.db import models

ORDERKEY_LENGTH = 32
SKU_LENGTH = 32
DEFAULT_CHAR_FIELD_MAX_LENGTH = 64


class Status(models.Model):
    status_name = models.CharField(
        max_length=DEFAULT_CHAR_FIELD_MAX_LENGTH,
        unique=True,
    )

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

    def __str__(self):
        return self.status_name


class Sku(models.Model):
    sku = models.CharField(
        max_length=SKU_LENGTH,
        unique=True,
    )

    class Meta:
        verbose_name = 'Складская единица товара'
        verbose_name_plural = 'Складские единицы товаров'

    def __str__(self):
        return self.sku


class OrderSku(models.Model):
    sku = models.ForeignKey(
        Sku,
        on_delete=models.CASCADE,
    )
    order = models.ForeignKey(
        'Pack',
        on_delete=models.CASCADE,
    )
    count = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Товары в заказе'
        verbose_name_plural = 'Заказы и товары'

    def __str__(self):
        return f'{self.order} - {self.count} {self.sku}'


class Pack(models.Model):
    orderkey = models.CharField(
        max_length=ORDERKEY_LENGTH,
        unique=True,
    )
    startpack = models.DateTimeField(null=True, blank=True)
    endpack = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
    )
    selected_carton = models.CharField(
        max_length=DEFAULT_CHAR_FIELD_MAX_LENGTH,
        blank=True,
    )
    recommended_carton = models.CharField(
        max_length=DEFAULT_CHAR_FIELD_MAX_LENGTH,
    )
    who = models.CharField(
        max_length=DEFAULT_CHAR_FIELD_MAX_LENGTH,
        blank=True,
    )
    sku_list = models.ManyToManyField(
        Sku,
        through=OrderSku,
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.orderkey
