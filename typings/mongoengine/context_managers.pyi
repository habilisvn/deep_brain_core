"""
This type stub file was generated by pyright.
"""

import contextlib
import threading
from contextlib import contextmanager

__all__ = ("switch_db", "switch_collection", "no_dereference", "no_sub_classes", "query_counter", "set_write_concern", "set_read_write_concern", "no_dereferencing_active_for_class")
class MyThreadLocals(threading.local):
    def __init__(self) -> None:
        ...
    


thread_locals = ...
def no_dereferencing_active_for_class(cls): # -> bool:
    ...

class switch_db:
    """switch_db alias context manager.

    Example ::

        # Register connections
        register_connection('default', 'mongoenginetest')
        register_connection('testdb-1', 'mongoenginetest2')

        class Group(Document):
            name = StringField()

        Group(name='test').save()  # Saves in the default db

        with switch_db(Group, 'testdb-1') as Group:
            Group(name='hello testdb!').save()  # Saves in testdb-1
    """
    def __init__(self, cls, db_alias) -> None:
        """Construct the switch_db context manager

        :param cls: the class to change the registered db
        :param db_alias: the name of the specific database to use
        """
        ...
    
    def __enter__(self): # -> Any:
        """Change the db_alias and clear the cached collection."""
        ...
    
    def __exit__(self, t, value, traceback): # -> None:
        """Reset the db_alias and collection."""
        ...
    


class switch_collection:
    """switch_collection alias context manager.

    Example ::

        class Group(Document):
            name = StringField()

        Group(name='test').save()  # Saves in the default db

        with switch_collection(Group, 'group1') as Group:
            Group(name='hello testdb!').save()  # Saves in group1 collection
    """
    def __init__(self, cls, collection_name) -> None:
        """Construct the switch_collection context manager.

        :param cls: the class to change the registered db
        :param collection_name: the name of the collection to use
        """
        ...
    
    def __enter__(self): # -> Any:
        """Change the _get_collection_name and clear the cached collection."""
        ...
    
    def __exit__(self, t, value, traceback): # -> None:
        """Reset the collection."""
        ...
    


@contextlib.contextmanager
def no_dereference(cls): # -> Generator[None, Any, None]:
    """no_dereference context manager.

    Turns off all dereferencing in Documents for the duration of the context
    manager::

        with no_dereference(Group):
            Group.objects()
    """
    ...

class no_sub_classes:
    """no_sub_classes context manager.

    Only returns instances of this class and no sub (inherited) classes::

        with no_sub_classes(Group) as Group:
            Group.objects.find()
    """
    def __init__(self, cls) -> None:
        """Construct the no_sub_classes context manager.

        :param cls: the class to turn querying subclasses on
        """
        ...
    
    def __enter__(self): # -> Any:
        """Change the objects default and _auto_dereference values."""
        ...
    
    def __exit__(self, t, value, traceback): # -> None:
        """Reset the default and _auto_dereference values."""
        ...
    


class query_counter:
    """Query_counter context manager to get the number of queries.
    This works by updating the `profiling_level` of the database so that all queries get logged,
    resetting the db.system.profile collection at the beginning of the context and counting the new entries.

    This was designed for debugging purpose. In fact it is a global counter so queries issued by other threads/processes
    can interfere with it

    Usage:

    .. code-block:: python

        class User(Document):
            name = StringField()

        with query_counter() as q:
            user = User(name='Bob')
            assert q == 0       # no query fired yet
            user.save()
            assert q == 1       # 1 query was fired, an 'insert'
            user_bis = User.objects().first()
            assert q == 2       # a 2nd query was fired, a 'find_one'

    Be aware that:

    - Iterating over large amount of documents (>101) makes pymongo issue `getmore` queries to fetch the next batch of documents (https://www.mongodb.com/docs/manual/tutorial/iterate-a-cursor/#cursor-batches)
    - Some queries are ignored by default by the counter (killcursors, db.system.indexes)
    """
    def __init__(self, alias=...) -> None:
        ...
    
    def __enter__(self): # -> Self:
        ...
    
    def __exit__(self, t, value, traceback): # -> None:
        ...
    
    def __eq__(self, value) -> bool:
        ...
    
    def __ne__(self, value) -> bool:
        ...
    
    def __lt__(self, value) -> bool:
        ...
    
    def __le__(self, value) -> bool:
        ...
    
    def __gt__(self, value) -> bool:
        ...
    
    def __ge__(self, value) -> bool:
        ...
    
    def __int__(self) -> int:
        ...
    
    def __repr__(self): # -> Any | str:
        """repr query_counter as the number of queries."""
        ...
    


@contextmanager
def set_write_concern(collection, write_concerns): # -> Generator[Any, Any, None]:
    ...

@contextmanager
def set_read_write_concern(collection, write_concerns, read_concerns): # -> Generator[Any, Any, None]:
    ...
