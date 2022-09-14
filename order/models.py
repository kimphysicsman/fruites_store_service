from django.db import models

from user.models import User as UserModel
from product.models import Price as PriceModel

class Order(models.Model):
    STATUS_CHOICES = (
        ("ready", "주문대기중"),
        ("cancel", "주문취소"),
        ("order_complete", "주문완료 & 결제 대기중"),
        ("pay_complete", "결제완료 & 배송 중"),
        ("delivery_complete", "배송 완료"),
    )

    user = models.ForeignKey(UserModel, verbose_name="주문자", on_delete=models.CASCADE)
    price = models.ManyToManyField(PriceModel, verbose_name="가격", through="PriceOrder")

    address = models.CharField("배송지", max_length=100)
    delivery_cost = models.IntegerField("배송비", default=0)
    total_price = models.IntegerField("총 가격", default=0)

    status = models.CharField("주문상태", max_length=20, choices=STATUS_CHOICES, default="ready")

    def __str__(self):
        return f"{self.user.username}'s order ({self.id})"

class PriceOrder(models.Model):
    order = models.ForeignKey(Order, verbose_name="주문", on_delete=models.CASCADE)
    price = models.ForeignKey(PriceModel, verbose_name="가격", on_delete=models.CASCADE)