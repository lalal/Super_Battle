import os
import django
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "super_battle.settings")
django.setup()

from clash.models import ComicZineFighter

a = open('data/other/o_0')
b = a.readlines()
data = json.loads(b[0])
res = data['results']
gender = ['Other', 'Male', 'Female']

for i in range(1, len(res)):
    f = ComicZineFighter()
    f.name = res[i]['name']
    f.publisher = res[i]['publisher']['name'] if res[i]['publisher'] else None
    f.date_last_updated = res[i]['date_last_updated']
    f.description = res[i]['description']
    f.deck = res[i]['deck']
    f.gender = gender[res[i]['gender']]
    f.image = res[i]['image']['medium_url'] if res[i]['image'] else None
    f.site_detail_url = res[i]['site_detail_url']
    f.api_detail_url = res[i]['api_detail_url']
    f.count_of_issue_appearances = res[i]['count_of_issue_appearances']
    f.first_appeared_in_issue = res[i]['first_appeared_in_issue']['api_detail_url'] if res[i]['first_appeared_in_issue'] else None
    f.birth = res[i]['birth']
    f.date_added = res[i]['date_added']
    f.real_name = res[i]['real_name']
    f.fighter_id = res[i]['id']
    f.aliases = res[i]['aliases'].replace('\n', ', ') if res[i]['aliases'] else None
    f.save()
#    for j in res[i]:
#        if j == 'publisher' and res[i][j]:
#            print j, res[i][j]['name']
#        elif j == 'image' and res[i][j]:
#            print j, res[i][j]['medium_url']
#        else:
#            print j, res[i][j]
    print f

       

        
    

