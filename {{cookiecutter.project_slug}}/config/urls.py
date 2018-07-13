from django.urls import include, path
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import verify_jwt_token
from config.routers import DefaultRouter

from project.users.urls import router as users_router

router = DefaultRouter()
router.extend(users_router)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('verify_token/', verify_jwt_token),
    path('', include('project.users.urls')),
    path('', include('project.api_registration.urls')),
    path('', include('drfpasswordless.urls')),
    path('docs/', include_docs_urls(title='{{cookiecutter.project_name}}')),
]
