from rest_framework import routers
from log.views import LogApiView

app_name = 'log'

router = routers.DefaultRouter()
router.register(r'calculadora', LogApiView, basename='calc')

urlpatterns = [
    
]
urlpatterns += router.urls