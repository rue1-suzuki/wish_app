from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE


class Wish(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=CASCADE,
        verbose_name='ユーザ',
    )

    title = models.CharField(
        verbose_name='商品名',
        max_length=128,
    )

    price = models.IntegerField(
        verbose_name='価格',
        default=0,
    )

    count = models.IntegerField(
        verbose_name='個数',
        default=0,
    )

    expected_buy_date = models.DateField(
        verbose_name='購入予定日',
        blank=True,
        null=True,
    )

    buy_date = models.DateField(
        verbose_name='購入日',
        blank=True,
        null=True,
    )

    shopname = models.CharField(
        verbose_name='店名',
        blank=True,
        null=True,
        max_length=128,
    )

    priority = models.IntegerField(
        verbose_name='優先度',
        choices=(
            (1, '低'),
            (2, '普通'),
            (3, '高'),
        ),
        default=2,
    )

    created_at = models.DateTimeField(
        verbose_name='作成日時',
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name='更新日時',
        auto_now=True,
    )
