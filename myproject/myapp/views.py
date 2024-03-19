import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def test_admin_email_handler(request):
    try:
        # This will intentionally raise an exception
        1 / 0
    except Exception as e:
        # Log the exception and include the request object as an extra parameter
        logger.error("An error occurred: %s", str(e))

    return HttpResponse("Test completed. Check your email for the error notification.")
