# -*- coding: utf-8 -*-
from django.shortcuts import render
# Добавлено:
from landing.forms import SubscriberForm

def landing(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid(): # пока в душе не знаю, нах.. эти две строчки
#        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()

    return render(request, 'landing/page.html', locals())