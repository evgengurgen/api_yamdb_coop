from django.urls import include, path
from rest_framework import routers

from users.views import SignupViewSet, TokenView
from .views import (CommentViewSet, ReviewViewSet,
                    TitleViewSet, CategoryViewSet, GenreViewSet)

router = routers.DefaultRouter()
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(
    r'titles',
    TitleViewSet,
    basename='titles'
)
router.register(
    r'categories',
    CategoryViewSet,
    basename='categories'
)
router.register(
    r'genres',
    GenreViewSet,
    basename='genres'
)
router.register(
    r'auth/signup',
    SignupViewSet,
    basename='signup'
)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', TokenView.as_view()),
]
