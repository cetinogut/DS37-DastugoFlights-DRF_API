"""dastugo_flight_booking_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from dastugo_user_api.views import logout_view
#from rest_framework_swagger.views import get_swagger_view
# drf_yasg code starts here
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#schema_view = get_swagger_view(title='Dastugo Flights API')
schema_view = get_schema_view(
    openapi.Info(
        title="Dastugo Flights API",
        default_version='v1',
        description="Welcome to the world of Dastugo",
        terms_of_service="https://www.dastugo.com",
        contact=openapi.Contact(email="admin@dastugo.com"),
        license=openapi.License(name="Dastugo LLC"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  #<-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  #
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  #
    #path('docs/', schema_view),  # swaggger, this did not worked so the lines above added
    path('admin/', admin.site.urls),
    path('', include('dastugo_user_api.urls')), # http://127.0.0.1:8000/register/
    path('user/', include('dastugo_user_api.urls')), # http://127.0.0.1:8000/user/register/
    path('', include('dastugo_flight_booking_api.urls')), # http://127.0.0.1:8000/flight/
    path('api/', include('dastugo_flight_booking_api.urls')), # http://127.0.0.1:8000/api/flight/
    path('logout/', logout_view, name='logout'), # overode in user_api
    
]
