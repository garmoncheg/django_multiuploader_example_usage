from django.shortcuts import render_to_response
from multiuploader.models import MultiuploaderImage


def image_view(request):
    items = MultiuploaderImage.objects.all()
    return render_to_response('images.html', {'items':items})


