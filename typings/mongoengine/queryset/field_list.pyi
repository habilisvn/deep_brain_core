"""
This type stub file was generated by pyright.
"""

__all__ = ("QueryFieldList", )
class QueryFieldList:
    """Object that handles combinations of .only() and .exclude() calls"""
    ONLY = ...
    EXCLUDE = ...
    def __init__(self, fields=..., value=..., always_include=..., _only_called=...) -> None:
        """The QueryFieldList builder

        :param fields: A list of fields used in `.only()` or `.exclude()`
        :param value: How to handle the fields; either `ONLY` or `EXCLUDE`
        :param always_include: Any fields to always_include eg `_cls`
        :param _only_called: Has `.only()` been called?  If so its a set of fields
           otherwise it performs a union.
        """
        ...
    
    def __add__(self, f): # -> Self:
        ...
    
    def __bool__(self): # -> bool:
        ...
    
    def as_dict(self): # -> dict[Any, int | Any]:
        ...
    
    def reset(self): # -> None:
        ...
    

