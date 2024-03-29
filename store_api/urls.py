from django.conf.urls import include, url
from store_api import views


urlpatterns = [
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^category/$', views.CategoryListView.as_view(), name='category'),
        url(r'^items/$', views.ItemListView.as_view(), name='item'),
        url(r'^item_detail/(?P<pk>[0-9]+)/$', views.ItemDetailView.as_view(), name='item-detail'),
        url(r'^add_item/$', views.ItemAddView.as_view(), name='add-item'),
        url(r'^add_category/$', views.CategoryAddView.as_view(), name='add-category'),
        url(r'^docs/', include('rest_framework_swagger.urls')),

]