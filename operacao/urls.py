from rest_framework import routers
from operacao.views import OperacaoApiView

app_name = 'operacao'

router = routers.DefaultRouter()
router.register(r'calculadora', OperacaoApiView, basename='calc')

urlpatterns = [
    
]
urlpatterns += router.urls