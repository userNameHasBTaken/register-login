from bbs import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login_acc',views.login_acc,name='login_acc'),
    url(r'^register_acc',views.register_acc,name='register_acc'),
    url(r'^logout_acc',views.logout_acc,name='logout_acc'),
]