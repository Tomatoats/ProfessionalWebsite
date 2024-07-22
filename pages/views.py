from django.shortcuts import render
from django.http import HttpResponse
from templates.pages import Compare,makegood
from pages import models
# Create your views here.
def load(request,dif1,same,dif2):
    print("we're in load")

    return render(request,"pages/compared.html",{})


def home(request):
    return render(request, "pages/home.html",{})


def spotify(request):
    if request.method == 'POST': # If the form has been submitted...
        print(request)
        playlists = request.POST.dict()
        play1 =playlists.get("play1")
        play2 =playlists.get("play2")
        #print(play1,play2)
        dif1,same,dif2 = Compare.getPlaylists(play1,play2)
        HttpResponse("pages/compared.html")
        objects = models.Testing(dif1,same,dif2)
        makegood.setup(objects)
        return render(request, "pages/compared.html",{})
    else:

        return render(request, "pages/compare.html",{})
    
        #form = ContactForm(request.POST) # A form bound to the POST data
        #if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

        #print form.cleaned_data['my_form_field_name']

        #return HttpResponseRedirect('/thanks/') # Redirect after POST
    #else:
        #form = ContactForm() # An unbound form

    #return render_to_response('contact.html', {
        #'form': form,
    #})


