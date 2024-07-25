import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pages import models
#getplaylists,clean,gettoken,compare,callSpotify Work
#now that we have id's, we can start making  the website


def toTest(p1,p2):
    tohave = "https://open.spotify.com/playlist/"
    if tohave in p1 and tohave in p2:
        return True
    else:
        return False


def dict_compare(d1, d2):
    set1 = set(d1.keys())
    set2 = set(d2.keys())
    intersection = set1.intersection(set2)
    difset1 = set1.difference(intersection)
    difset2 = set2.difference(intersection)
    same = {}
    for x in d1,intersection:
        if intersection(x) == x.keys():
            same.update({intersection(x):(x.values())})
            x.popitem()
    print(same)
#TODO: So we can still have our regular compare go on , i think I get the ID's, and then just get the info i need as a dict after that cause this is shit man  



def addtoModels(dif1,same,dif2,songs):
    print("got to models!")
    d1dict = {}
    d1 = []
    sdict = {}
    sm = []
    d2dict = {}
    d2 = []

    for x in same:
        sm = songs.get(x)
        sdict.update({x:sm})
        #cover = result['image']

    for x in dif1:
        d1 = songs.get(x)
        #print(result)

        d1dict.update({x:d1})
        #cover = result['images']['url']
    for x in dif2:
        d2 = songs.get(x)
        #print(result)

        d2dict.update({x:d2})

    #model = models.Global(len(dif1),len(same),len(dif2))
    #model.save()
    #print("Add to models numbers: ", len(sdict),len(d1dict),len(d2dict))

   #for key, value in d1dict.items():
        #print(f"{key}: {value}")
    #return d1dict,sdict,d2dict



def clean(playlist):
     play = playlist[34:] #chopping off the htps:// open.spotify shenanigans
     p =  play[:22] # sometimes there's more than meets the eye
     return p


def getToken():
    clid = "432742e8cdd04d149d847dd79a797024"
    clet = "69a867f4a0544550bf6c10e2f94b26c2"
    yuri = "http://alexys.online/projects/Compare"
    scope = ""
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=clid,client_secret=clet))
    return sp

    #sp_oauth = SpotifyOAuth(client_id=clid,client_secret=clet,redirect_uri=yuri)
    #access_token = sp_oauth.get_access_token()
    #refresh_token = sp_oauth.get_refresh_token()
    #return access_token


def compare(id1,id2):
    set1 = set(id1)
    set2 = set(id2)
    intersection = set1.intersection(set2)
    difset1 = set1.difference(intersection)
    difset2 = set2.difference(intersection)

    dif1 = list(difset1)
    dif2 = list(difset2)
    same = list(intersection)

    # to test if they all up
    print( len(dif1),len(same), len(dif2))

    #addtoModels(dif1,same,dif2)
    return dif1,same,dif2




def callSpotify(p,thisdict):
    offset = 0
    sp = getToken()
    print(sp)
    #data = access_token.json()
    #print(data["error"])
    


    flag = True
    songids = []
    #results = sp.playlist_items(p,offset=offset,fields='items.track',additional_types=['track'])
    #result = json.dumps(results, indent=2)
    #fileout = open("out.JSON","w+")
    #fileout.write(result)
    #print(results)
    #if len(results['items']) == 0:
    #flag = False
    count = 0
    while flag == True:
    
        #results = sp.playlist_items(p2,offset=offset,fields='items.track.name.total',additional_types=['track'])
        results = sp.playlist_items(p,offset=offset,fields='items.track',additional_types=['track'])
        
        
        if len(results['items']) == 0:
            flag = False
        
        

        
        offset = offset + len(results['items'])
        
        
        for idx, track in enumerate(results['items']):
            listing = []
            
            songids.append(str(track['track']['id']))
            pid = str(track['track']['id']) #pid
            listing.append(str(track['track']['name'])) #name
            listing.append(str(track['track']['artists'][0]['name'])) #artist
            listing.append(str(track['track']['preview_url'])) #audio
            listing.append(str(track['track']['album']['images'][2]['url'])) #album
            

            #increment = 100*count + idx
            #print("New Song!: ID:",pid)
            #print("Name:", name)
            #print(artist)
            #print(audio)
            #print(album)
            #thisdict.update({"id":pid,"name":name,"artist":artist,"audio":audio,"album":album})

            #thisdict.update({increment:pid{{"name":name},{"artist":artist},{"audio":audio},{"album":album}}})
            thisdict.update({pid:listing})
           
            #print("toadd and increment:",toAdd,increment)
        count +=1
    #print(thisdict.items())
    return songids,thisdict


    

def getPlaylists(play1,play2):
    p1 = clean(play1)
    p2 = clean(play2)
    songdict= {}
    id1,songdict =  callSpotify(p1,songdict)
    id2,songdict = callSpotify(p2,songdict)
    #dict_compare(dict1,dict2)
    #print(id1,id2)
    print("okay this is dict1:",len(songdict))
    
    dif1, same, dif2 = compare(id1,id2)
    addtoModels(dif1,same,dif2,songdict)
    return dif1,same,dif2,songdict
    #todo: Have a dict for all the song stuff we need, sets to show, and then we go down and find all the dict for said lists so that we don't have to results twice
    
    #print(len(dif1),len(same), len(dif2), "second time!")

