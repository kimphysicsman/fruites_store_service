from django.urls import path


from product.views import ProductView, PriceView


# /order
urlpatterns = [
    path('', ProductView.as_view()),
]