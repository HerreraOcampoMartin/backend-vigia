from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from common.token_management import CustomTokenObtainPairView

urlpatterns = [
    # JWT Authentication
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # TODO: custom refresh token to not allow deleted accounts to refresh its token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('admin/', admin.site.urls),

    # API User
    path('api/usuarios/', include('users.urls', namespace='usuarios')),

    # API amenazas
    path('api/', include('amenazas.urls', namespace='amenazas')),

    # API alertas
    path('api/', include('alertas.urls', namespace='alertas')),

    # Allow API debug login
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
