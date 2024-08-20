from rest_framework.routers import DefaultRouter

from shortener.views import UrlViewSet

core_router = DefaultRouter()
core_router.register(r"url-view", UrlViewSet, basename="url-view")
url_patterns = core_router.urls

url_patterns += [

]