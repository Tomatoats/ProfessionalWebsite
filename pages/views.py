from django.shortcuts import render
from django.http import HttpResponse
from templates.pages import Compare,makegood
from django.contrib import messages
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
        try:
            #dif1,same,dif2,length,biglength,a = Compare.getPlaylists(play1,play2)
            ultlist,length,biglength,a = Compare.getPlaylists(play1,play2)
        except:
            return render(request,"pages/compare.html",{"badmessage":"These don't seem to be spotify links. Please use a link to a spotify playlist!"})
        else:
        #print(play1,play2)
            
            #messages.info(request,'These links aren\'t spotify playlists. Try using the links of the playlist!')
            #return render(request,"pages/compare.html",{"badmessage":"These don't seem to be spotify links. Please use a link to a spotify playlist!"})
            
            #TODO: Send a little message popup
            #dif1,same,dif2,songdict = Compare.getPlaylists(play1,play2)
        #dict1= dict(dif1)
        #print(dict1)
            HttpResponse("pages/compared.html")
            #objects = models.Testing(dif1,same,dif2,songdict)
            #makegood.setup(objects)
            print("rendeerrr")
            #return render(request, "pages/compared.html",{"length":length,"dif1":dif1,"same":same,"dif2":dif2,"biglength":biglength,"a":a})
            return render(request, "pages/compared.html",{"length":length,"ultlist":ultlist,"biglength":biglength,"a":a})
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


