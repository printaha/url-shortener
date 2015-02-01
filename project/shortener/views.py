from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from shortener.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

# Create your views here.
def index(request):
  return render(request, "shortener/index.html")

def shorten(request):
  context = RequestContext(request)
  full_URL = request.POST['url']
  context['full_URL'] = full_URL
  context['short_id'] = 'jeejee'
  return render_to_response("shortener/index.html", context)

def getURL(request, id):
  try:
    URL_entry = URL.objects.get(short_id = id)
    full_URL = URL_entry.full_URL
    return HttpResponseRedirect(full_URL)
  except ObjectDoesNotExist:
    raise Http404("Corresponding URL to given ID not found")
  return render(request, "shortener/index.html")