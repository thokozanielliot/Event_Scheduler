from django.urls import path, include
from accounts import views
from rest_framework.routers import DefaultRouter

app_name = 'accounts'

router =DefaultRouter()
router.register("",views.UserViewSet, 'accounts')

urlpatterns = [
    #path('', views.all_users, name='all-users'),
    path('', include('rest_framework.urls')),
]
urlpatterns += router.urls
