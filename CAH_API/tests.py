import json
from CAH_API.models import BlackCard, WhiteCard

json_file = open('CAH_API/static/CAH_API/cah.json')
json_data = json.load(json_file)
json_file.close()

count = 0
for black_card in json_data['blackCards']:
    count += 1
    black_card = BlackCard(text=black_card['text'], pick=black_card['pick'], id=count)
    black_card.save()

count = 0
for white_card in json_data['whiteCards']:
    count += 1
    white_card = WhiteCard(text=white_card, id=count)
    white_card.save()

# WhiteCard.cards.all().delete()
# BlackCard.cards.all().delete()
