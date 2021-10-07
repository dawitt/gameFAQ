from django.shortcuts import render
import requests
import json
# Create your views here.


def console_detail_view(request, id):
    url = 'https://api.rawg.io/api/platforms/' + str(id)
    headers={
        'User-Agent': 'Q4_Capstone',
    }
    payload={
        'key':'81ea352e06b54bb4b1218cb8d2b0e4eb',        
    }
    response = requests.get(url, headers=headers, params=payload)
    data = json.loads(response.text)
    console_name = data['name']
    console_slug = data['slug']
    console_img = data['image_background']
    console_desc = data['description']
    games_count = data['games_count']
    data = json.dumps(data, indent=2)
    return render(request, 'console.html', {'data': data, 'console_name':console_name, 'console_img': console_img, 'console_desc': console_desc, 'games_count':games_count, 'console_slug':console_slug ,'id':id})


def console_games_view(request, console):
    if console == 'pc':
        id = 4
        console_name = 'PC'
    elif console == 'playstation5':
        id = 187
        console_name = 'Play Station 5'
    elif console == 'playstation4':
        id = 18
        console_name = 'Play Station 4'
    elif console == 'nintendo-switch':
        id = 7
        console_name = 'Nintendo Switch'
    elif console == 'xbox-one':
        id = 1
        console_name = 'XBOX ONE'
    elif console == 'xbox-series-x':
        id = 186
        console_name = 'XBOX SERIES S/X'
    url = 'https://api.rawg.io/api/games'
    headers={
        'User-Agent': 'Q4_Capstone',
    }
    payload={
        'key':'81ea352e06b54bb4b1218cb8d2b0e4eb',
        'platforms': id
    }
    response = requests.get(url, headers=headers, params=payload)
    data = json.loads(response.text)
    game_list = []
    for game in data['results']:
        print(game['slug'])
        game_obj = {
            'game_name': game['name'],
            'game_slug': game['slug'],
            'game_img': game['background_image']
        }
        game_list.append(game_obj)
    # game_platforms = 
    data = json.dumps(data, indent=2)
    print(url)
    return render(request, 'console_all_games.html', {'data': data, 'id':id, 'game_list':game_list, 'console':console_name})
    #'game_name':game_name, 'game_slug':game_slug, 'game_img':game_img

