from django.conf.urls import url
from registers import views

urlpatterns=[
    url(r'^api/registers$',views.registers_list),
    url(r'^api/registers/(?P<pk>[0-9]+)$',views.registers_detail),    
]