# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import gettext_lazy as _


class DjangoCMSFormsApphook(CMSApp):
    name = _("Forms")
    urls = ["djangocms_forms.urls"]


apphook_pool.register(DjangoCMSFormsApphook)
