import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from my_app.models import *
from my_app.models import Album

# Create your views here.
# def index (request): 
#     albums = Album.objects.all()
#     songs =Song.objects.all()
#     my_data={'albums' : albums, 'songs': songs}
#     return render(request, 'my_app/index.html', context= my_data )
@csrf_exempt
def albums(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data["name"]
        album = Album(name= name)
        album.save()

        my_data ={"album": album.serialize()}
    else:
            
        if request.GET.get("album_id") is not None:
            album_id = request.GET["album_id"]
            album= Album.objects.get(id=album_id).serialize()
            my_data = {"album": album}

        else:
            albums = list(Album.objects.all().values("id", "name"))
            my_data={"albums": albums , "hi": [123, 234, 444]}
    return JsonResponse(my_data)

def album_details(request):
    album_id = request.GET["album_id"]
    album= Album.objects.get(id=album_id).values()
    return JsonResponse({"album": album})

def index(request):
    name = request.GET["name"]
    return HttpResponse( f"hello {name}")