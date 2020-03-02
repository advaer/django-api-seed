class BaseService:
    """
    Intermediate placeholder layer for custom project-wide methods and attributes
    """
    pass


class GenericBaseService(BaseService):
    """
    Generic Service for database CRUD operations
    """
    model_class = None

    @classmethod
    def get_list(cls):
        return cls.model_class.objects.all()

    @classmethod
    def get_object(cls, pk):
        return cls.model_class.objects.get_object(pk)

    @classmethod
    def create_object(cls, data):
        obj = cls.model_class(**data)
        obj.save()
        return obj

    @classmethod
    def update_object(cls, pk, data):
        """
        Update object, keep immutable 'created' but update 'modified'
        """
        obj = cls.model_class.objects.get_object(pk=pk)
        for key, value in data.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    @classmethod
    def delete_object(cls, pk):
        obj = cls.get_object(pk)
        obj.delete()
