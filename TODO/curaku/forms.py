from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.models import User
from .models import Task


class DateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'due_date', 'completed']  # Exclude 'user'
        widgets = {
            'due_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TaskForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['user'].queryset = User.objects.filter(id=user.id)
        if 'user' in self.fields:
            self.fields['user'].widget = forms.HiddenInput()


class YourForm(forms.ModelForm):
    # ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))  # If this line exists, it adds a submit button.
