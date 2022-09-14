from django.db import models

from order.models import Order as OrderModel

class Payment(models.Model):
    METHOD_CHOISE = (
        ("card", "신용카드"),
        ("credit", "현금"),
        ("point", "포인트"),
        ("kakaopay", "카카오페이")
    )

    STATUS_CHOISE = (
        ("ready", "결제 대기중"),
        ("cancel", "결제 취소"),
        ("complete", "결제 완료")
    )

    order = models.ForeignKey(OrderModel, verbose_name="주문", on_delete=models.CASCADE)
    price = models.IntegerField("결제금액")
    method = models.CharField("결제방법", max_length=100, choices=METHOD_CHOISE)
    status = models.CharField("결제상태", max_length=100, choices=STATUS_CHOISE)