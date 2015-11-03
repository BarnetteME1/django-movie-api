import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from movie.models import Movie

__author__ = 'MatthewBarnette'

@csrf_exempt
def api_movie_list_create(request):
    if request.POST:
        title = request.POST.get('title')
        Movie.objects.create(title=title)
        return HttpResponse(json.dumps({'message':'Title added'}), content_type='application/json')
    all_movies = Movie.objects.all()
    data = json.dumps([{'id': all_movies.id, 'title': all_movies.title} for all_movies in all_movies])
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def api_movie_detail(request, pk,):
    if request.method == 'DELETE':
        Movie.objects.get(id=pk).delete()
        return HttpResponse('DELETED!')
    movie = Movie.objects.get(id=pk)
    serialize_movie = json.dumps({'id': movie.id, 'title': movie.title})
    return HttpResponse(serialize_movie, content_type='application/json')

