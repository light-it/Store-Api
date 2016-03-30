from django.conf.urls import include, url
from store_api import views


urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'category/$', views.CategoryListView.as_view(), name='category'),
        url(r'items/$', views.ItemListView.as_view(), name='item'),
        url(r'item_detail/(?P<pk>[0-9]+)/$', views.ItemDetailView.as_view(), name='item-detail'),
        url(r'^docs/', include('rest_framework_swagger.urls')),

]