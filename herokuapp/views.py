from django.shortcuts import render
from django.views import View
from herokuapp import models

# Create your views here.
class Hello(View):
    def get(self, request):
        a = models.Thing()
        a.save()
        b = models.Thing.objects.all()

        return render(request,"hello.html",{"times":b})