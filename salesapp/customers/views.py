from django.views.generic import TemplateView


class DashboardTemplateView(TemplateView):
    template_name = "customers/dashboard.html"
