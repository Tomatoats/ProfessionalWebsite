import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pages import models
#getplaylists,clean,gettoken,compare,callSpotify Work
#now that we have id's, we can start making  the website


def addtoModels(dif1,same,dif2):
    sp = getToken()
    d1map = {}
    d1 = []
    smap = {}
    sm = []
    d2map = {}
    d2 = []
    for x in dif1:
        result = sp.track(x)
        #print(result)
        d1map['ID'] = x
        d1map['name'] = result['name']
        d1map['audio'] = result['preview_url']
        d1.append(d1map)
        #cover = result['images']['url']
    for x in same:
        result = sp.track(x)
        smap['ID'] = x
        smap['name'] = result['name']
        smap['audio'] = result['preview_url']
        sm.append(smap)
        #cover = result['image']
    for x in dif2:
        result = sp.track(x)
        #print(result)
        d2map['ID'] = x
        d2map['name'] = result['name']
        d2map['audio'] = result['preview_url']
        d2.append(d2map)

    #model = models.Global(len(dif1),len(same),len(dif2))
    #model.save()
    pass



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




def callSpotify(p):
    offset = 0
    sp = getToken()
    print(sp)
    #data = access_token.json()
    #print(data["error"])
    


    flag = True
    songids = []
    #results = sp.playlist_items(p2,offset=offset,fields='items.track.name.total',additional_types=['track'])
    #result = json.dumps(results, indent = 4)
    #if len(results['items']) == 0:
    #flag = False
    
    while flag == True:

        #results = sp.playlist_items(p2,offset=offset,fields='items.track.name.total',additional_types=['track'])
        results = sp.playlist_items(p,offset=offset,fields='items.track.id.total',additional_types=['track'])
        if len(results['items']) == 0:
            flag = False
        result =  json.dumps(results, indent = 4)
        res = json.loads(result)
        #print(results['items'])

        #print(len(results['items']))
        
        offset = offset + len(results['items'])
        
        #print(offset, "/", results['items'])
        #print(results['items'])
        #print(offset, "/", results['items'])
        
        for idx, track in enumerate(results['items']):
            #print(idx,track)
            songids.append(str(track)[18:40])
            #print(str(track)[18:40])

    #pass
    #print(songids)
    return songids
    
    
    #string = "https://api.spotify.com/v1/playlists/"
    #header = "Authorization: Bearer  BQDBKJ5eo5jxbtpWjVOj7ryS84khybFpP_lTqzV7uV-T_m0cTfwvdn5BnBSKPxKgEb11"
    #url = string+p1
    #print(url)
    #response = requests.get(url)
    #return response
    #print(response)
    #pass

def getPlaylists(play1,play2):
    p1 = clean(play1)
    p2 = clean(play2)
    id1 =  callSpotify(p1)
    id2 = callSpotify(p2)
    dif1,same,dif2 = compare(id1,id2)
    return dif1,same,dif2

    
    #print(len(dif1),len(same), len(dif2), "second time!")

