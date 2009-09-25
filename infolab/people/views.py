from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, get_object_or_404


from people.models import Person, Paper

def index(request):
    faculty = Person.objects.filter(grouping__exact='fac').order_by("last_name")
    phds = Person.objects.filter(grouping__exact='PhD').order_by("last_name")
    masters = Person.objects.filter(grouping__exact='Mas').order_by("last_name")
    return render_to_response('people/list.html', {'section': 'people',
        'faculty':faculty,
        'phds':phds,
        'masters':masters
        })


def publist(request):
    return render_to_response('people/publist.html', {'section':'pub', 'pubs':Paper.objects.all()})


def detail(request, uname):
    user = get_object_or_404(Person, username=uname)
    return render_to_response('people/detail.html', {'person':user, 'section': 'people'})
