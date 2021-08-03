from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'Home/index.html')

def zen(request):
    import this
    zen = ''
    for char in this.s:
        if char in this.d:
            zen += this.d[char]
        else: zen += char
    context = {'zen': zen}
    return render(request, 'Home/zen.html', context)

def oops(request, resource):
    return render(request, 'oops.html')
