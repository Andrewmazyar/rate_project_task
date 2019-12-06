from django.views.generic import ListView, CreateView
from .models import RateCourse
from .forms import RateCourseForm
from django.urls import reverse


class RateCourseView(ListView):
    model = RateCourse
    context_object_name = 'rates'
    template_name = 'index.html'


class RateCourseCreate(CreateView):
    model = RateCourse
    form_class = RateCourseForm
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('index.html', args=(self.object.id,))

