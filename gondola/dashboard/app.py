from django.contrib.admin.views.decorators import staff_member_required

from oscar.core.application import Application

from .urls import urlpatterns


class GondolaDashboardApplication(Application):
    name = None

    def get_urls(self):
        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = GondolaDashboardApplication()