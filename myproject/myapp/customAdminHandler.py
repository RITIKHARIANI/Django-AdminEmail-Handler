from django.utils.log import AdminEmailHandler
from django.core.mail import EmailMessage
from django.conf import settings
import logging

class CustomAdminEmailHandler(AdminEmailHandler):
    def emit(self, record):
        return super().emit(record)
