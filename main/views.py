from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Главная"
        context["content"] = "Магазин мебели HOME"
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
class DeliveryView(TemplateView):
    template_name = "main/delivery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
class ContactsView(TemplateView):
    template_name = "main/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
