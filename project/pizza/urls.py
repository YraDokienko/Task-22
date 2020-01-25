from django.urls import path, include
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from .views_drf import PizzaViewSet, CartViewSet, PizzaFilterView, PizzaToCartView

router = routers.DefaultRouter()
router.register('pizza_list', PizzaViewSet)
router.register('cart_list', CartViewSet)
router.register('filter', PizzaFilterView, basename='Pizza')
router.register('pizza_to_cart', PizzaToCartView)

urlpatterns = [
    path('', cache_page(60*1)(views.PizzaHomeView.as_view()), name='home'),
    path('pizza-form-add/', views.PizzaFormAddView.as_view(), name='pizza_add'),
    path('cart/', views.PizzaCartView.as_view(), name='cart'),
    path('stop_spam_page/', TemplateView.as_view(template_name='stop_spam_page.html')),
    path('pizza-price-update/', views.PizzaPriceUpdateView.as_view(), name='price_update'),
    path('add-pizza-to-order/', views.AddPizzaToOrderView.as_view()),
    path('cart/shipping/', views.ShippingOrderView.as_view(), name='shipping'),
    path('cart/shipping/create/', views.HomePageCreateOrder.as_view(), name='create'),
    path('del_instance/<int:id>', views.AddPizzaToOrderView.del_instance, name='delete'),
    path('pizza-update/<int:pk>/edit/', views.PizzaUpdateView.as_view(), name='pizza_update'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
