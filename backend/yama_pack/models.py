from django.db import models

ORDERKEY_LENGTH = 32
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
        blank=True,
    )
    who = models.CharField(
        max_length=DEFAULT_CHAR_FIELD_MAX_LENGTH,
        blank=True,
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.orderkey


class RepackingCargotype(models.Model):
    cargotype = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Карготип с доупаковкой'
        verbose_name_plural = 'Карготипы с доупаковкой'

    def __str__(self):
        return f'{self.cargotype}'
