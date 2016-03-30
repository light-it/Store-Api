from django.conf.urls import include, url
from store_api import views


urlpatterns = [
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^docs/', include('rest_framework_swagger.urls')),

]