from django.urls import path


from product.views import ProductView, PriceView


# /product
urlpatterns = [
    path('', ProductView.as_view()),
    path('/<id>', ProductView.as_view()),
    path('/<id>/price', PriceView.as_view()),
    path('/price/<id>', PriceView.as_view()),
]