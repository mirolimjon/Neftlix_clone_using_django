from  django.urls import path
from .views import Home, ProfileList, ProfileCreate, MovieList, MovieDetail, MoviePlay

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("profile", ProfileList.as_view(), name="profile"),
    path("profile/create", ProfileCreate.as_view(), name="create"),
    path("watch/<str:profile_id>", MovieList.as_view(), name="movie-list"),
    path("watch/detail/<str:movie_id>", MovieDetail.as_view(), name="movie-detail"),
    path("watch/play-movie/<str:movie_id>", MoviePlay.as_view(), name="play-movie"),
]