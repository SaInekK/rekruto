from django.http import HttpResponse

# Create your views here.
from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        name = request.GET.get('name')
        message = request.GET.get('message')
        return HttpResponse(f"<span style=\"white-space: pre-line\">Hello {name}!\n{message}!</span>")
