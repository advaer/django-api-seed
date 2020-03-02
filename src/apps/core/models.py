from django.db import models


class BaseModel(models.Model):
    """
    Intermediate placeholder layer for custom project-wide methods and attributes
    """

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    @classmethod
    def get_update_fields(cls, data):
        """
        Helper function
        Adds service field 'modified' to update_fields list
        """
        update_fields = list(data.keys())
        update_fields.append('modified')
        return update_fields

    class Meta:
        abstract = True
