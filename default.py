import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import requests
import json

# Получаем настройки аддона
addon = xbmcaddon.Addon()
moode_host = addon.getSetting('moode_host')

BASE_URL = f"http://{moode_host}"

def get_radio_stations():
    url = f"{BASE_URL}/command/radio.php?cmd=get_stations"
    response = requests.get(url)
    return response.json()

def get_music_library():
    url = f"{BASE_URL}/command/music-library.php?cmd=load_library"
    response = requests.get(url)
    return response.json()

def get_player_status():
    url = f"{BASE_URL}/engine-mpd.php"
    response = requests.get(url)
    return response.json()

def play_radio(station_url):
    url = f"{BASE_URL}/command/queue.php?cmd=clear_play_item"
    data = {'path': station_url}
    response = requests.post(url, data=data)

def play_album(track_paths):
    url = f"{BASE_URL}/command/queue.php?cmd=clear_play_group"
    data = {'path[]': track_paths}
    response = requests.post(url, data=data)

def play():
    url = f"{BASE_URL}/engine-mpd.php?state=play"
    response = requests.get(url)

def stop():
    url = f"{BASE_URL}/engine-mpd.php?state=stop"
    response = requests.get(url)

def pause():
    url = f"{BASE_URL}/engine-mpd.php?state=pause"
    response = requests.get(url)

def list_radio_stations():
    stations = get_radio_stations()
    for station in stations:
        list_item = xbmcgui.ListItem(label=station['name'])
        list_item.setInfo('music', {'genre': station['genre'], 'artist': station['broadcaster']})
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=station['station'], listitem=list_item, isFolder=False)
    xbmcplugin.endOfDirectory(addon_handle)

def list_music_library():
    library = get_music_library()
    for item in library:
        list_item = xbmcgui.ListItem(label=item['title'])
        list_item.setInfo('music', {'artist': item['album_artist'], 'album': item['album']})
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=item['file'], listitem=list_item, isFolder=False)
    xbmcplugin.endOfDirectory(addon_handle)

def route(path):
    if path == '/':
        # Main menu
        xbmcplugin.setContent(addon_handle, 'music')
        xbmcplugin.endOfDirectory(addon_handle)
    elif path == '/radio':
        list_radio_stations()
    elif path == '/library':
        list_music_library()

if __name__ == '__main__':
    addon_handle = int(sys.argv[1])
    args = sys.argv[2][1:]
    route(args)
