from django import forms


INTERVAL_CHOICES = [
    ('1', 'Uma vez por dia'),
    ('2', 'Duas vezes por dia'),
    ('3', 'Três vezes por dia'),
    ('4', 'Uma vez por semana'),
]


class SetIntervalForm(forms.Form):
    interval = forms.CharField(
        label='Informe o intervalo para envio das mensagens',
        required=True,
        widget=forms.Select(
            choices=INTERVAL_CHOICES,
            attrs={

            }
        )
    )

    def __init__(self, user, *args, **kwargs):
        super(SetIntervalForm, self).__init__(*args, **kwargs)
        self.fields['interval'].initial = user.interval
