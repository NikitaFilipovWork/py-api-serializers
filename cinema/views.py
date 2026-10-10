from rest_framework import viewsets
from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession,
)
from cinema.serializers import (
    GenreSerializer,
    ActorSerializer,
    MovieSerializer,
    MovieListSerializer,
    CinemaHallSerializer, ActorListSerializer, MovieSessionSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ActorListSerializer
        return ActorSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            queryset = queryset.select_related("movie", "cinema_hall")
        return queryset
