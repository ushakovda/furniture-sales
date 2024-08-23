from django.urls import path

from orders import views

app_name = "goods"

urlpatterns = [
    path("create-order/", views.create_order, name="create_order"),
]
