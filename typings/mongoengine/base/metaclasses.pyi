"""
This type stub file was generated by pyright.
"""

__all__ = ("DocumentMetaclass", "TopLevelDocumentMetaclass")
class DocumentMetaclass(type):
    """Metaclass for all documents."""
    def __new__(mcs, name, bases, attrs):
        ...
    


class TopLevelDocumentMetaclass(DocumentMetaclass):
    """Metaclass for top-level documents (i.e. documents that have their own
    collection in the database.
    """
    def __new__(mcs, name, bases, attrs):
        ...
    
    @classmethod
    def get_auto_id_names(mcs, new_class): # -> tuple[Literal['id'], Literal['_id']] | tuple[str, str] | None:
        """Find a name for the automatic ID field for the given new class.

        Return a two-element tuple where the first item is the field name (i.e.
        the attribute name on the object) and the second element is the DB
        field name (i.e. the name of the key stored in MongoDB).

        Defaults to ('id', '_id'), or generates a non-clashing name in the form
        of ('auto_id_X', '_auto_id_X') if the default name is already taken.
        """
        ...
    


class MetaDict(dict):
    """Custom dictionary for meta classes.
    Handles the merging of set indexes
    """
    _merge_options = ...
    def merge(self, new_options): # -> None:
        ...
    


class BasesTuple(tuple):
    """Special class to handle introspection of bases tuple in __new__"""
    ...

