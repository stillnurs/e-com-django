from django.urls import path

from vendor import views


urlpatterns = [
    path('stock-list/', views.StockListAPIView.as_view()),
    path('stock-detail/<int:id>', views.StockDetailAPIView.as_view()),
]
