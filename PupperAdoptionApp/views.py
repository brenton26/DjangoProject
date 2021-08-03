from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .api_service import *
from .models import Dog, TempDog
from .forms import DogForm
from datetime import datetime


# Create your views here.
class Index(View):

    def get(self, request):
        dog_info = get_dog_info()
        dogs = create_dog_dict_entry(dog_info)
        context = {'dogs': dogs}

        TempDog.dogs.all().delete()
        for key, value in dogs.items():
            dog = TempDog()
            dog.id = value['id']
            dog.breed = value['breed']
            dog.breed_group = value['breed_group']
            dog.height = value['height']
            dog.weight = value['weight']
            dog.life_span = value['life_span']
            dog.image = value['image']
            dog.save()
        return render(request, 'PupperAdoptionApp/adopt_index.html', context)

    def post(self, request):
        return render(request, 'PupperAdoptionApp/adopt_form.html')
    

def adopt(request, id):
    dog = TempDog.dogs.get(id=id)
    context = {
        'id': id,
        'breed': dog.breed,
        'adoption_date': datetime.now().strftime("%m/%d/%Y"),
        'breed_group': dog.breed_group,
        'height': dog.height,
        'weight': dog.weight,
        'life_span': dog.life_span,
        'image': dog.image,
    }
    form = DogForm(request.POST or None, initial=context)
    context['form'] = form
    if form.is_valid():
        form.save()
        return redirect('pups')
    else:
        print(form.errors)
    return render(request, 'PupperAdoptionApp/adopt_form.html', context)


def pups(request):
    get_pups = Dog.dogs.all()
    context = {'dogs': get_pups}
    return render(request, 'PupperAdoptionApp/pups.html', context)


def pup_trash(request, id):
    pup = get_object_or_404(Dog, pk=id)
    if request.method == 'POST':
        pup.delete()
        return redirect('pups')
    return render(request, "PupperAdoptionApp/pup_trash.html", context={'pup': pup})

