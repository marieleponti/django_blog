from django.shortcuts import render
from django.http import HttpResponse

post = [
    {
        'author': 'Mari',
        'title': 'Blog Post 1',
        'content': 'Everything is content.',
        'date_posted': '31 August 2022'
    },
    {
        'author': 'Jesse',
        'title': 'Self care and empowerment',
        'content': 'Collective care and real power.',
        'date_posted': '1 September 2022'
    }
]


def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')