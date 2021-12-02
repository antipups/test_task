from django.urls import include, path
from rest_framework import routers
from WorkApp import views

router = routers.DefaultRouter()
router.register(r'legals', views.LegalSet)
router.register(r'clients', views.ClientSet)
router.register(r'deps', views.DepartmentSet)


urlpatterns = [
    path('', include(router.urls))
]
