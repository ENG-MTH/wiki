import random

from django.shortcuts import redirect
from django.shortcuts import render

from . import util
from .forms import EntryCreateForm


def index(request):
    q = request.GET.get('q')
    entries = util.list_entries()
    if q:
        entries = [e for e in entries if q.lower() in e.lower()]
    if q in entries:
        return redirect('wiki:single-entry', q)
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })


def single_entery(request, title: str):
    content = util.get_entry(title)
    if not content:
        return render(request, 'encyclopedia/error.html', {
            'title': '404'
        })
    return render(request, 'encyclopedia/single_entry.html', {
        'title': title,
        'content': content
    })


def create_entry(request):
    """

    @type request: object
    """
    form = EntryCreateForm()

    if request.method == 'POST':
        form = EntryCreateForm(request.POST)
        if form.is_valid():
            title, content = form.cleaned_data['title'], form.cleaned_data['content']
            if title in util.list_entries():
                return render(request, 'encyclopedia/error.html', {
                    'title': f'The entry {title} already exists'
                })
            util.save_entry(title, content)

            return redirect('wiki:index')

    return render(request, 'encyclopedia/create_entry.html', {
        'form': form,
    })


def edit_entry(request, title: str):
    return None


def random_entry(request):
    entries = util.list_entries()
    random_choice = random.choice(entries)
    return redirect('wiki:single-entry', random_choice)
