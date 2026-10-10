from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    MovieViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
)

app_name = "cinema"

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("movies", MovieViewSet)
router.register("cinema-halls", CinemaHallViewSet)
router.register("movie-sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
