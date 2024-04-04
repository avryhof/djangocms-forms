# -*- coding: utf-8 -*-

from django.urls import path

from .views import FormSubmission

# This is ugly, but I gather there are still people running outdated Django versions.

urlpatterns = [
    path("forms/submit/", FormSubmission.as_view(), name="djangocms_forms_submissions"),
]
