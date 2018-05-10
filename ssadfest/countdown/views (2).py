from django.shortcuts import render
from .forms import MemberForm


def index(request):
    return render(request, 'countdown/index.html')


def member_new(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.email = request.email
            member.name = request.name
            member.city = request.city
            member.company = request.company
            member.specialization = request.specialization
            member.regdate = timezone.now()
            member.save()
            return redirect('index', pk=member.pk)
    else:
        form = MemberForm()
    return render(request, 'countdown/registration.html', {'form': form})

