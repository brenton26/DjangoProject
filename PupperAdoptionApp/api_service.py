import requests
import random

# API Keys
DOG_API_KEY = 'a214cce1-92a0-42e3-a7f6-1c8c140cb6c4'


def get_dog_info():
    url = 'https://api.thedogapi.com/v1/breeds'
    headers = {
        'x-api-key': DOG_API_KEY
    }
    raw_dog_json_data = requests.request("GET", url, headers=headers).json()

    NUM_DOGS_IN_RANDOM_SAMPLE = 10
    random_sample_of_dogs = random.sample(raw_dog_json_data, NUM_DOGS_IN_RANDOM_SAMPLE)
    return(random_sample_of_dogs)


def create_dog_dict_entry(dog_sample):
    organized_dog_data = {}
    count = 0
    for dog in dog_sample:
        count += 1
        entry = {
            'id': count,
            'breed': dog.get('name'),
            'breed_group': dog.get('breed_group'),
            'height': dog.get('height').get('imperial') + ' in',
            'weight': dog.get('weight').get('imperial') + ' lbs',
            'image': dog.get('image').get('url'),
            'life_span': dog.get('life_span'),
        }
        organized_dog_data[count] = entry
    return organized_dog_data





