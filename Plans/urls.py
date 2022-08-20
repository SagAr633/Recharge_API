from Plans import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('plans', views.PlansViewSet, basename='all_plans'),

urlpatterns = [

]+router.urls