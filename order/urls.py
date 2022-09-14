from django.urls import path


from order.views import OrderView, OrderPriceView


# /order
urlpatterns = [
    path('', OrderView.as_view()),
    path('/<id>', OrderView.as_view()),
    path('/<order_id>/add/<price_id>', OrderPriceView.as_view()),
]