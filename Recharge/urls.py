from Recharge import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('recharge', views.RechargeViewSet, basename='all_plans'),

urlpatterns = [

]+router.urls