from django.db import models


class BaseManager(models.Manager):
    """
    Intermediate placeholder layer for custom project-wide methods and attributes
    """
    def get_object(self, pk):
        try:
            obj = self.get(pk=pk)
        except self.model.DoesNotExist:
            raise KeyError
        return obj
