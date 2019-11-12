from django.utils.deprecation import MiddlewareMixin
import settings

class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(request.get_host())
        domain_parts = request.get_host().split('.')
        domain_parts[0] = domain_parts[0].lower()
        wwwPresent = False
        try:
            domain_parts.remove('www')
            wwwPresent = True
        except:
            pass
        if wwwPresent:
            if domain_parts[0] != settings.MAIN_DOMAIN:
                subdomain = domain_parts[0]
            else:
                subdomain = None
        else:
            if domain_parts[0] != settings.MAIN_DOMAIN:
                subdomain = domain_parts[0]
            else:
                subdomain = None

        request.subdomain = subdomain


        print(subdomain)
