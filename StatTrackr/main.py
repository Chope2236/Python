import requests
import json

data = requests.get('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=C16DC689A5D1F1F7DB696FE23B5D3CA4&steamid=76561198961737375').json()
##beautified_data = (json.dumps(data, sort_keys=True, indent=4))
for stat in data["playerstats"]["stats"]:
    if stat["name"] == "last_match_kills":
       k = stat["value"]
    if stat["name"] == "last_match_deaths":
       d = stat["value"]
kd = ("{:.1f}".format(k/d))

