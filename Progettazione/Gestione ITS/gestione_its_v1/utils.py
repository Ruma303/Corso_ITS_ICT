from __future__ import annotations


class MyObject(object):
    __all_objects: dict[str, MyObject] = dict()

    @classmethod
    def all_objects(cls) -> dict[str, MyObject]:
        return cls.__all_objects

    @classmethod
    def get_object(cls, key: str):
        return cls.__all_objects[key]

    def __repr__(self):
        return f"{self.__class__.__name__}"
