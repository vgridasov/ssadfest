#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .forms import MemberForm
from .models import Member
#from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'countdown/index.html')


#def members(request):
#    s_title = 'Участники'
#    members = Member.objects.all()
#    return render(request, 'countdown/members.html', context={'members': members, 's_title': s_title})


class Members(generic.ListView):
    template_name = 'countdown/members.html'
    context_object_name = 'members'

    def get_queryset(self):
        return Member.objects.all()


def member_new(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()
            return HttpResponseRedirect('/members/')
    else:
        form = MemberForm()
    return render(request, 'countdown/registration.html', {'form': form})

