
from django.contrib import admin
from django.urls import path, include
from bestitem.views import index
from rest_framework import routers
import bestitem.views

router = routers.DefaultRouter()
router.register("deals", bestitem.views.DealViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bestitem.views.index, name='index.html'),
    path('api/', include(router.urls))

]
