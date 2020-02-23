# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View

class TopPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app_folder/top_page.html')

top_page = TopPageView.as_view()