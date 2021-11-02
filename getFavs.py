import tidalapi

favFile = ''

def getItemIds(favItems):

    for i in favItems:
        print(i.id)

def addFavs(favs):

    with open(favFile) as favTracks:
        for line in favTracks:
            track = line.rstrip()
            print(track)
            favs.add_track(track)

if __name__ == "__main__":

    session = tidalapi.Session()
    # Will run until you visit the printed url and link your account
    session.login_oauth_simple()
    user_id = session.user.id
    favs = tidalapi.Favorites(session, user_id)
    res = addFavs(favs)
