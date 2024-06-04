from django.shortcuts import render

# Create your views here.
def digitalClock(request):
  context = {
    'title': 'Digital Clock'
  }
  return render(request, 'digitalClock/digitalClock.html', context)