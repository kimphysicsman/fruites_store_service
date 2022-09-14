from django.db import models

class Product(models.Model):
    STATUS_CHOICES = (
        ("ready", "판매준비중"),
        ("sale", "판매중"),
        ("soldout", "판매완료"),
    )

    name = models.CharField("이름", max_length=20)
    description = models.CharField("설명", max_length=200, default="")
    address = models.CharField("판매지", max_length=100, default="")
    delivery_cost = models.IntegerField("배송비", default=0)
    status = models.CharField("판매상태", max_length=20, choices=STATUS_CHOICES, default="ready")

    def __str__(self):
        return f"{self.id} - {self.name}"


class Price(models.Model):
    product = models.ForeignKey(Product, verbose_name="상품", on_delete=models.CASCADE)
    unit = models.CharField("판매단위", max_length=100)
    price = models.IntegerField("가격")
    stock = models.IntegerField("재고", default=0)

    def __str__(self):
        return f"{self.product.name} : {self.unit} - {str(self.price)}"