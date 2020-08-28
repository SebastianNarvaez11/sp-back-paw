from rest_framework import routers
from .views import GradeViewSet

router = routers.DefaultRouter()
router.register('grade', GradeViewSet)

urlpatterns = router.urls
