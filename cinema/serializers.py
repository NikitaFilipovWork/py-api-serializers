from rest_framework import serializers
from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession,
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    movies = serializers.CharField(source="movie__title", read_only=True)

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name", "movies"]


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "full_name"]

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        ]


class MovieListSerializer(MovieSerializer):
    genres = serializers.CharField(source="genres__name", read_only=True)
    actors = serializers.CharField(source="actors__full_name", read_only=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        ]


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row"]


class MovieSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
