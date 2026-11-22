from . import views
from django.urls import path    

urlpatterns = [
    path('token/',view=views.LoginView.as_view(),name='login'),
    
    path('product/',view=views.ProductListCreateApiView.as_view(),name='create-list-product'),
    path('product/<uuid:uuid>/',view=views.ProductUpdateDestroyApiView.as_view(),name='update-delete-product'),
    
    path('movimentation/',view=views.MovimentationListCreateAPIView.as_view(),name='create-list-product'),
    path('product/baixo-minimo/',view=views.AbaixoDoMinimoListAPIView.as_view(),name='products-below-minimum')
]