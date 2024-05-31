
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from . import views

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secureomar/', admin.site.urls),
    path("graphql", GraphQLView.as_view(graphiql=True)),
    path('',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('metting/',views.new_meeting,name='new_meeting'),
    path('join/',views.join_meeting,name='join_meeting'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)