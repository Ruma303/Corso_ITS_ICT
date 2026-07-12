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
        result = cls._objects_by_uuid.values()
        if result is None:
          return None
        return result

    @classmethod
    def get_object_by_uuid(cls, k: UUID) -> Optional[Self]:
        result = cls._objects_by_uuid.get(k)
        if result is None:
          return None
        return result


class ClassUtilsNomi:
    _objects_by_name: dict[str, Self]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._objects_by_name = {}

    @classmethod
    def all_objects_by_nome(cls):
        result = cls._objects_by_name.values()
        if result is None:
          return None
        return result

    @classmethod
    def get_object_by_nome(cls, nome: str) -> Optional[Self]:
      result = cls._objects_by_name.get(nome)
      if result is None:
        return None
      return result


class ClassUtilsCF:
    _objects_by_cf: dict[CodiceFiscale, Self]

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._objects_by_cf = {}

    @classmethod
    def all_objects_by_cf(cls):
        result = cls._objects_by_cf.values()
        if result is None:
          return None
        return result

    @classmethod
    def get_object_by_cf(cls, cf: CodiceFiscale) -> Optional[Self]:
        result = cls._objects_by_cf.get(cf)
        if result is None:
          return None
        return result

