"""
This type stub file was generated by pyright.
"""

from mongoengine.base import BaseDocument, DocumentMetaclass, TopLevelDocumentMetaclass

__all__ = ("Document", "EmbeddedDocument", "DynamicDocument", "DynamicEmbeddedDocument", "OperationError", "InvalidCollectionError", "NotUniqueError", "MapReduceDocument")
def includes_cls(fields):
    """Helper function used for ensuring and comparing indexes."""
    ...

class InvalidCollectionError(Exception):
    ...


class EmbeddedDocument(BaseDocument, metaclass=DocumentMetaclass):
    r"""A :class:`~mongoengine.Document` that isn't stored in its own
    collection.  :class:`~mongoengine.EmbeddedDocument`\ s should be used as
    fields on :class:`~mongoengine.Document`\ s through the
    :class:`~mongoengine.EmbeddedDocumentField` field type.

    A :class:`~mongoengine.EmbeddedDocument` subclass may be itself subclassed,
    to create a specialised version of the embedded document that will be
    stored in the same collection. To facilitate this behaviour a `_cls`
    field is added to documents (hidden though the MongoEngine interface).
    To enable this behaviour set :attr:`allow_inheritance` to ``True`` in the
    :attr:`meta` dictionary.
    """
    __slots__ = ...
    my_metaclass = DocumentMetaclass
    __hash__ = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __getstate__(self): # -> dict[Any, Any]:
        ...
    
    def __setstate__(self, state): # -> None:
        ...
    
    def to_mongo(self, *args, **kwargs): # -> SON[Any, Any]:
        ...
    


class Document(BaseDocument, metaclass=TopLevelDocumentMetaclass):
    """The base class used for defining the structure and properties of
    collections of documents stored in MongoDB. Inherit from this class, and
    add fields as class attributes to define a document's structure.
    Individual documents may then be created by making instances of the
    :class:`~mongoengine.Document` subclass.

    By default, the MongoDB collection used to store documents created using a
    :class:`~mongoengine.Document` subclass will be the name of the subclass
    converted to snake_case. A different collection may be specified by
    providing :attr:`collection` to the :attr:`meta` dictionary in the class
    definition.

    A :class:`~mongoengine.Document` subclass may be itself subclassed, to
    create a specialised version of the document that will be stored in the
    same collection. To facilitate this behaviour a `_cls`
    field is added to documents (hidden though the MongoEngine interface).
    To enable this behaviour set :attr:`allow_inheritance` to ``True`` in the
    :attr:`meta` dictionary.

    A :class:`~mongoengine.Document` may use a **Capped Collection** by
    specifying :attr:`max_documents` and :attr:`max_size` in the :attr:`meta`
    dictionary. :attr:`max_documents` is the maximum number of documents that
    is allowed to be stored in the collection, and :attr:`max_size` is the
    maximum size of the collection in bytes. :attr:`max_size` is rounded up
    to the next multiple of 256 by MongoDB internally and mongoengine before.
    Use also a multiple of 256 to avoid confusions.  If :attr:`max_size` is not
    specified and :attr:`max_documents` is, :attr:`max_size` defaults to
    10485760 bytes (10MB).

    Indexes may be created by specifying :attr:`indexes` in the :attr:`meta`
    dictionary. The value should be a list of field names or tuples of field
    names. Index direction may be specified by prefixing the field names with
    a **+** or **-** sign.

    Automatic index creation can be disabled by specifying
    :attr:`auto_create_index` in the :attr:`meta` dictionary. If this is set to
    False then indexes will not be created by MongoEngine.  This is useful in
    production systems where index creation is performed as part of a
    deployment system.

    By default, _cls will be added to the start of every index (that
    doesn't contain a list) if allow_inheritance is True. This can be
    disabled by either setting cls to False on the specific index or
    by setting index_cls to False on the meta dictionary for the document.

    By default, any extra attribute existing in stored data but not declared
    in your model will raise a :class:`~mongoengine.FieldDoesNotExist` error.
    This can be disabled by setting :attr:`strict` to ``False``
    in the :attr:`meta` dictionary.
    """
    my_metaclass = TopLevelDocumentMetaclass
    __slots__ = ...
    @property
    def pk(self): # -> Any | None:
        """Get the primary key."""
        ...
    
    @pk.setter
    def pk(self, value): # -> None:
        """Set the primary key."""
        ...
    
    def __hash__(self) -> int:
        """Return the hash based on the PK of this document. If it's new
        and doesn't have a PK yet, return the default object hash instead.
        """
        ...
    
    def to_mongo(self, *args, **kwargs): # -> SON[Any, Any]:
        ...
    
    def modify(self, query=..., **update): # -> bool:
        """Perform an atomic update of the document in the database and reload
        the document object using updated version.

        Returns True if the document has been updated or False if the document
        in the database doesn't match the query.

        .. note:: All unsaved changes that have been made to the document are
            rejected if the method returns True.

        :param query: the update will be performed only if the document in the
            database matches the query
        :param update: Django-style update keyword arguments
        """
        ...
    
    def save(self, force_insert=..., validate=..., clean=..., write_concern=..., cascade=..., cascade_kwargs=..., _refs=..., save_condition=..., signal_kwargs=..., **kwargs):
        """Save the :class:`~mongoengine.Document` to the database. If the
        document already exists, it will be updated, otherwise it will be
        created. Returns the saved object instance.

        :param force_insert: only try to create a new document, don't allow
            updates of existing documents.
        :param validate: validates the document; set to ``False`` to skip.
        :param clean: call the document clean method, requires `validate` to be
            True.
        :param write_concern: Extra keyword arguments are passed down to
            :meth:`~pymongo.collection.Collection.save` OR
            :meth:`~pymongo.collection.Collection.insert`
            which will be used as options for the resultant
            ``getLastError`` command.  For example,
            ``save(..., write_concern={w: 2, fsync: True}, ...)`` will
            wait until at least two servers have recorded the write and
            will force an fsync on the primary server.
        :param cascade: Sets the flag for cascading saves.  You can set a
            default by setting "cascade" in the document __meta__
        :param cascade_kwargs: (optional) kwargs dictionary to be passed throw
            to cascading saves.  Implies ``cascade=True``.
        :param _refs: A list of processed references used in cascading saves
        :param save_condition: only perform save if matching record in db
            satisfies condition(s) (e.g. version number).
            Raises :class:`OperationError` if the conditions are not satisfied
        :param signal_kwargs: (optional) kwargs dictionary to be passed to
            the signal calls.

        .. versionchanged:: 0.5
            In existing documents it only saves changed fields using
            set / unset.  Saves are cascaded and any
            :class:`~bson.dbref.DBRef` objects that have changes are
            saved as well.
        .. versionchanged:: 0.6
            Added cascading saves
        .. versionchanged:: 0.8
            Cascade saves are optional and default to False.  If you want
            fine grain control then you can turn off using document
            meta['cascade'] = True.  Also you can pass different kwargs to
            the cascade save using cascade_kwargs which overwrites the
            existing kwargs with custom values.
        .. versionchanged:: 0.26
           save() no longer calls :meth:`~mongoengine.Document.ensure_indexes`
           unless ``meta['auto_create_index_on_save']`` is set to True.

        """
        ...
    
    def cascade_save(self, **kwargs): # -> None:
        """Recursively save any references and generic references on the
        document.
        """
        ...
    
    def update(self, **kwargs):
        """Performs an update on the :class:`~mongoengine.Document`
        A convenience wrapper to :meth:`~mongoengine.QuerySet.update`.

        Raises :class:`OperationError` if called on an object that has not yet
        been saved.
        """
        ...
    
    def delete(self, signal_kwargs=..., **write_concern): # -> None:
        """Delete the :class:`~mongoengine.Document` from the database. This
        will only take effect if the document has been previously saved.

        :param signal_kwargs: (optional) kwargs dictionary to be passed to
            the signal calls.
        :param write_concern: Extra keyword arguments are passed down which
            will be used as options for the resultant ``getLastError`` command.
            For example, ``save(..., w: 2, fsync: True)`` will
            wait until at least two servers have recorded the write and
            will force an fsync on the primary server.
        """
        ...
    
    def switch_db(self, db_alias, keep_created=...): # -> Self:
        """
        Temporarily switch the database for a document instance.

        Only really useful for archiving off data and calling `save()`::

            user = User.objects.get(id=user_id)
            user.switch_db('archive-db')
            user.save()

        :param str db_alias: The database alias to use for saving the document

        :param bool keep_created: keep self._created value after switching db, else is reset to True


        .. seealso::
            Use :class:`~mongoengine.context_managers.switch_collection`
            if you need to read from another collection
        """
        ...
    
    def switch_collection(self, collection_name, keep_created=...): # -> Self:
        """
        Temporarily switch the collection for a document instance.

        Only really useful for archiving off data and calling `save()`::

            user = User.objects.get(id=user_id)
            user.switch_collection('old-users')
            user.save()

        :param str collection_name: The database alias to use for saving the
            document

        :param bool keep_created: keep self._created value after switching collection, else is reset to True


        .. seealso::
            Use :class:`~mongoengine.context_managers.switch_db`
            if you need to read from another database
        """
        ...
    
    def select_related(self, max_depth=...): # -> Self:
        """Handles dereferencing of :class:`~bson.dbref.DBRef` objects to
        a maximum depth in order to cut down the number queries to mongodb.
        """
        ...
    
    def reload(self, *fields, **kwargs): # -> Self:
        """Reloads all attributes from the database.

        :param fields: (optional) args list of fields to reload
        :param max_depth: (optional) depth of dereferencing to follow
        """
        ...
    
    def to_dbref(self): # -> DBRef:
        """Returns an instance of :class:`~bson.dbref.DBRef` useful in
        `__raw__` queries."""
        ...
    
    @classmethod
    def register_delete_rule(cls, document_cls, field_name, rule): # -> None:
        """This method registers the delete rules to apply when removing this
        object.
        """
        ...
    
    @classmethod
    def drop_collection(cls): # -> None:
        """Drops the entire collection associated with this
        :class:`~mongoengine.Document` type from the database.

        Raises :class:`OperationError` if the document has no collection set
        (i.g. if it is `abstract`)
        """
        ...
    
    @classmethod
    def create_index(cls, keys, background=..., **kwargs):
        """Creates the given indexes if required.

        :param keys: a single index key or a list of index keys (to
            construct a multi-field index); keys may be prefixed with a **+**
            or a **-** to determine the index ordering
        :param background: Allows index creation in the background
        """
        ...
    
    @classmethod
    def ensure_indexes(cls): # -> None:
        """Checks the document meta data and ensures all the indexes exist.

        Global defaults can be set in the meta - see :doc:`guide/defining-documents`

        By default, this will get called automatically upon first interaction with the
        Document collection (query, save, etc) so unless you disabled `auto_create_index`, you
        shouldn't have to call this manually.

        This also gets called upon every call to Document.save if `auto_create_index_on_save` is set to True

        If called multiple times, MongoDB will not re-recreate indexes if they exist already

        .. note:: You can disable automatic index creation by setting
                  `auto_create_index` to False in the documents meta data
        """
        ...
    
    @classmethod
    def list_indexes(cls): # -> list[Any]:
        """Lists all indexes that should be created for the Document collection.
        It includes all the indexes from super- and sub-classes.

        Note that it will only return the indexes' fields, not the indexes' options
        """
        ...
    
    @classmethod
    def compare_indexes(cls): # -> dict[str, list[Any]]:
        """Compares the indexes defined in MongoEngine with the ones
        existing in the database. Returns any missing/extra indexes.
        """
        ...
    


class DynamicDocument(Document, metaclass=TopLevelDocumentMetaclass):
    """A Dynamic Document class allowing flexible, expandable and uncontrolled
    schemas.  As a :class:`~mongoengine.Document` subclass, acts in the same
    way as an ordinary document but has expanded style properties.  Any data
    passed or set against the :class:`~mongoengine.DynamicDocument` that is
    not a field is automatically converted into a
    :class:`~mongoengine.fields.DynamicField` and data can be attributed to that
    field.

    .. note::

        There is one caveat on Dynamic Documents: undeclared fields cannot start with `_`
    """
    my_metaclass = TopLevelDocumentMetaclass
    _dynamic = ...
    def __delattr__(self, *args, **kwargs): # -> None:
        """Delete the attribute by setting to None and allowing _delta
        to unset it.
        """
        ...
    


class DynamicEmbeddedDocument(EmbeddedDocument, metaclass=DocumentMetaclass):
    """A Dynamic Embedded Document class allowing flexible, expandable and
    uncontrolled schemas. See :class:`~mongoengine.DynamicDocument` for more
    information about dynamic documents.
    """
    my_metaclass = DocumentMetaclass
    _dynamic = ...
    def __delattr__(self, *args, **kwargs): # -> None:
        """Delete the attribute by setting to None and allowing _delta
        to unset it.
        """
        ...
    


class MapReduceDocument:
    """A document returned from a map/reduce query.

    :param collection: An instance of :class:`~pymongo.Collection`
    :param key: Document/result key, often an instance of
                :class:`~bson.objectid.ObjectId`. If supplied as
                an ``ObjectId`` found in the given ``collection``,
                the object can be accessed via the ``object`` property.
    :param value: The result(s) for this key.
    """
    def __init__(self, document, collection, key, value) -> None:
        ...
    
    @property
    def object(self):
        """Lazy-load the object referenced by ``self.key``. ``self.key``
        should be the ``primary_key``.
        """
        ...
    

