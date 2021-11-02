import tidalapi

session = tidalapi.Session()
# Will run until you visit the printed url and link your account
session.login_oauth_simple()

def getItemIds(favItems):

    for i in favItems:
        print(i.id)

if __name__ == "__main__":

    user_id = session.user.id

    favs = tidalapi.Favorites(session, user_id)

    #favsracks = tidalapi.Favorites(session, user_id)

    favTracks = favs.tracks()

    favAlbums = favs.albums()

    favPlaylists = favs.playlists()

    print("tracks")
    tracksItemIds = getItemIds(favTracks)
    print("albums")
    albumItemIds = getItemIds(favAlbums)
    print("playlists")
    playlistsItemIds = getItemIds(favPlaylists)