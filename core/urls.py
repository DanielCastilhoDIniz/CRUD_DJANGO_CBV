from django.urls import path

from .views import IndexView, ProdutoCreateView, ProdutoUpdateView
from .views import ProdutoDeleteView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', ProdutoCreateView.as_view(), name='add_produto'),
    path('update/<int:pk>/', ProdutoUpdateView.as_view(),
         name='update_produto'),
    path('delete/<int:pk>/', ProdutoDeleteView.as_view(),
         name='delete_produto')
]
