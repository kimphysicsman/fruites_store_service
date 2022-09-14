from django.urls import path

from payment.views import PaymentView


# /payment
urlpatterns = [
    path('', PaymentView.as_view()),

]