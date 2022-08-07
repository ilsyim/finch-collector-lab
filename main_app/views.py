from django.shortcuts import render
from django.http import HttpResponse

class Finch:
  def __init__(self, name, description, age):
    self.name = name
    self.description = description
    self.age = age

finches= {
  Finch('birb', 'tiny birb', 3),
  Finch('BIRD', 'tiny birb', 0),
  Finch('birb', 'tiny birb', 1)
}

# Create your views here.
def home(request):
  return HttpResponse('<h1>This is the home page!!</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', {'finches': finches})