from typing import Optional, Self
from uuid import UUID
from datatypes import CodiceFiscale


class ClassUtilsUUID:
    _objects_by_uuid: dict[UUID, Self]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._objects_by_uuid = {}

    @classmethod
    def all_objects_by_uuid(cls):
        return cls._objects_by_uuid.values()
        

    @classmethod
    def get_object_by_uuid(cls, k: UUID) -> Optional[Self]:
        return cls._objects_by_uuid.get(k)
        


class ClassUtilsNomi:
    _objects_by_name: dict[str, Self]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._objects_by_name = {}

    @classmethod
    def all_objects_by_nome(cls):
        return cls._objects_by_name.values()

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Optional[Self]:
      return cls._objects_by_name.get(nome)
      


class ClassUtilsCF:
    _objects_by_cf: dict[CodiceFiscale, Self]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._objects_by_cf = {}

    @classmethod
    def all_objects_by_cf(cls):
        return cls._objects_by_cf.values()
        

    @classmethod
    def get_object_by_cf(cls, cf: CodiceFiscale) -> Optional[Self]:
        return cls._objects_by_cf.get(cf)
        