from django.urls import path, include
from items.views import HomeView, ItemUpdateView, ItemCreateView, SearchItemView, SearchCategoryView, SearchPriceView, ItemActionView, RentListView, SearchLocationView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('item/create/', ItemCreateView.as_view(), name='item-create'), 
    path('item/search/', SearchItemView.as_view(), name='search'),
    path('item/city/search', SearchCategoryView.as_view(), name='search_category'),
    path('item/price/search', SearchPriceView.as_view(), name='search_price'),
    path('item/location/search', SearchLocationView.as_view(), name='search_location'),
    path("item/<int:pk>/actions/accept/<int:rental_pk>/", ItemActionView.as_view(action="accept"), name="item_accept"),
    path("item/<int:pk>/actions/reject/<int:rental_pk>/", ItemActionView.as_view(action="reject"), name="item_reject"),
    path("item/<int:pk>/actions/cancel/<int:rental_pk>/", ItemActionView.as_view(action="cancel"), name="cancel_request"),
    path("item/<int:pk>/actions/switchrent/", ItemActionView.as_view(action="switchrent"), name="switchrent"),
    path("item/<int:pk>/actions/rent/", ItemActionView.as_view(action="rent"), name="item_rent"),
    path("item/<int:pk>/remove/", ItemActionView.as_view(action="remove", validate=True), name="item_remove"),
    path("item/rentrequests/", RentListView.as_view(), name='rent_requests'),
    path('item/update/<slug:itemslug>', ItemUpdateView.as_view(), name='item-update'),

]
