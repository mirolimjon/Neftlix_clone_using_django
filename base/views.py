from django.shortcuts import render, redirect
from .models import CustomUser, Profile, Movies, Video
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("profile")
        return render(request, "index.html")


method_decorator(login_required, name="dispatch")
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()

        context = {
            'profiles': profiles
        }

        return render(request, 'profilelist.html', context)


method_decorator(login_required, name="dispatch")
class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        context = {
            'form': form
        }   
        return render(request, 'profilecreate.html', context)

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect("profile")

        context = {
            'form': form
        }        
        return render(request, 'profilecreate.html', context)


method_decorator(login_required, name="dispatch")
class MovieList(View):
    def get(self, request, profile_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(uuid=profile_id)
            movies = Movies.objects.filter(age_limit = profile.age_limit)
            if profile not in request.user.profiles.all():
                return redirect('profile')

            context = {
                'movies': movies
            }    
            return render(request, 'movieList.html', context)
        except Profile.DoesNotExist:
            return redirect('profile')

method_decorator(login_required, name="dispatch")
class MovieDetail(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movies.objects.get(uuid=movie_id)
            context = {
                'movie': movie
            }    
            return render(request, 'movieDetail.html', context)
        except Movies.DoesNotExist:
            return redirect('profile')            



method_decorator(login_required, name="dispatch")
class MoviePlay(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movies.objects.get(id=movie_id)
            movie = movie.video.values()
            context = {
                'movie': list(movie)
            }    
            return render(request, 'playmovie.html', context)
        except Movies.DoesNotExist:
            return redirect('profile')       