from .models import RateCourse
from django.forms import ModelForm


class RateCourseForm(ModelForm):
    class Meta:
        model = RateCourse
        fields = (
            'uah',
            'timestamp',
        )