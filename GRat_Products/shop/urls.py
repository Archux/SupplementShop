from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path
from . import views
from .views import HomeView, SpecialDealsView, ProteinPowdersView, PreWorkoutView, CreatineView, \
MassGainersView, BarsAndSnacksView, VitaminsView, ProductDetails, SearchProductsView


admin.site.site_header = "G-Rat Products"
admin.site.index_title = "Admin page"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('special_deals/', SpecialDealsView.as_view(), name="special_deals"),
    path('protein_powders/', ProteinPowdersView.as_view(), name="protein_powders"),
    path('pre_workout/', PreWorkoutView.as_view(), name="pre_workout"),
    path('creatine/', CreatineView.as_view(), name="creatine"),
    path('mass_gainers/', MassGainersView.as_view(), name="mass_gainers"),
    path('bars_and_snacks/', BarsAndSnacksView.as_view(), name="bars_and_snacks"),
    path('vitamins/', VitaminsView.as_view(), name="vitamins"),
    path('search_products/', SearchProductsView.as_view(), name="search_products"),
    path('products/<int:pk>/', ProductDetails.as_view(), name='product_details'),
    path('cart/', views.cart, name="cart"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
