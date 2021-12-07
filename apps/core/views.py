from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.core.forms import SetIntervalForm


@login_required
def index(request):
    form = SetIntervalForm(data=request.POST or None, user=request.user)

    if form.is_valid():
        interval = form.cleaned_data.get('interval')
        request.user.update_interval(interval)

        return redirect('core:index')

    return render(request, 'core/index.html', {'form': form})
