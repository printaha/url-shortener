from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from shortener.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

# Create your views here.
def index(request):
  return render(request, "shortener/index.html")

# This creates a new database entry every time you submit the form (if something was entered into the text field in index.html)
# You might not want to flood the database endlessly in a "real" service
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

# If a URL is found with the given id in /get/id, the user is 301 redirected to the specified URL
# Note that HttpResponsePermanentRedirect will not redirect you to a different domain if you don't specify your URL with http:// or https:// etc at the start
def getURL(request, id):
  try:
    URL_entry = URL.objects.get(pk = id)
    full_URL = URL_entry.full_URL
    return HttpResponsePermanentRedirect(full_URL)
  except (ValueError, ObjectDoesNotExist):
    raise Http404("Corresponding URL to given ID not found")
  return render(request, "shortener/index.html")