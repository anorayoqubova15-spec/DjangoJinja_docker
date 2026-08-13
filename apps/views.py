from django.shortcuts import render


def home(request):
    return render(
        request,
        "index.html",
        {
            "name": "Anora",
            "title": "Django + Jinja2"
        }
    )