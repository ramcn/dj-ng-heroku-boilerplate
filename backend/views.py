from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request, template_name="index.html"):
    """
    The index view which serves the Angular.js SPA. The path to the correct
    index.html is configured in /config/settings.py with the SPA_INDEX
    variable.
    """
    return render_to_response(template_name,
                              context_instance=RequestContext(request))
