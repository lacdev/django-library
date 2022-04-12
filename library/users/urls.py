from library.users import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
	path('login', views.LoginView.as_view()),
	path('logout', views.LogoutView.as_view()),
	path('', include(router.urls)),
]