from .models import SiteConfig

def site_config(request):
    """
    Returns the singleton SiteConfig object.
    """
    config = SiteConfig.objects.first()
    return {'site_config': config}
