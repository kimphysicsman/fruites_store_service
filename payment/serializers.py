from rest_framework import serializers

from payment.models import Payment as PaymentModel


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = "__all__"