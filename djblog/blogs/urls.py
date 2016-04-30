
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = DefaultRouter()
router.register(r'blogs', views.BlogViewSet)
router.register(r'blogs/(?P<blog_id>[0-9]+)', views.BlogViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'comments', views.CommentViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
	url(r'^', include(router.urls) ),
]

#urlpatterns = format_suffix_patterns(urlpatterns)