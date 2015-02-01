from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from shortener.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

# Create your views here.
def index(request):
  return render(request, "shortener/index.html")

def shorten(request):
  context = RequestContext(request)
  if request.method == 'POST':
    long_URL = request.POST['url']
    if long_URL == '':
      return HttpResponseRedirect("/")
    u = URL(full_URL=long_URL)
    u.save()
    id_str = str(u.pk)
    return HttpResponse(id_str)
  return HttpResponseRedirect("/")

def getURL(request, id):
  try:
    URL_entry = URL.objects.get(pk = id)
    full_URL = URL_entry.full_URL
    return HttpResponsePermanentRedirect(full_URL)
  except (ValueError, ObjectDoesNotExist):
    raise Http404("Corresponding URL to given ID not found")
  return render(request, "shortener/index.html")