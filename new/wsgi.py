"""
WSGI config for new project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


#http_proxy  = "172.16.63.15:3128"
#https_proxy = "172.16.63.15:3128"


#proxyDict = {
              #"http"  : http_proxy,
             # "https" : https_proxy,

            #}

#os.environ["PROXIES"] = proxyDict

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "new.settings")

application = get_wsgi_application()
