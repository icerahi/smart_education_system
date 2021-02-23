from django.apps import AppConfig


class NodeActivityConfig(AppConfig):
    name = 'apps.node_activity'

    def ready(self):
        from . import signals
        from .models import ActiveNode
        ActiveNode.objects.all().delete()




