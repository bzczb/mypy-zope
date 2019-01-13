# Stubs for zope.schema._bootstrapinterfaces (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import zope.interface
from typing import Any, Optional

class StopValidation(Exception): ...

class ValidationError(zope.interface.Invalid):
    field: Any = ...
    value: Any = ...
    def with_field_and_value(self, field: Any, value: Any): ...
    def doc(self): ...
    def __lt__(self, other: Any): ...
    def __eq__(self, other: Any): ...
    __hash__: Any = ...

class RequiredMissing(ValidationError):
    __doc__: Any = ...

class WrongType(ValidationError):
    __doc__: Any = ...
    expected_type: Any = ...
    value: Any = ...
    def __init__(self, value: Optional[Any] = ..., expected_type: Optional[Any] = ..., name: Optional[Any] = ..., *args: Any) -> None: ...

class OutOfBounds(ValidationError):
    bound: Any = ...
    TOO_LARGE: Any = ...
    TOO_SMALL: Any = ...
    violation_direction: Any = ...
    value: Any = ...
    def __init__(self, value: Optional[Any] = ..., bound: Optional[Any] = ..., *args: Any) -> None: ...

class OrderableOutOfBounds(OutOfBounds): ...

class TooBig(OrderableOutOfBounds):
    __doc__: Any = ...
    violation_direction: Any = ...

class TooSmall(OrderableOutOfBounds):
    __doc__: Any = ...
    violation_direction: Any = ...

class LenOutOfBounds(OutOfBounds): ...

class TooLong(LenOutOfBounds):
    __doc__: Any = ...
    violation_direction: Any = ...

class TooShort(LenOutOfBounds):
    __doc__: Any = ...
    violation_direction: Any = ...

class InvalidValue(ValidationError):
    __doc__: Any = ...

class ConstraintNotSatisfied(ValidationError):
    __doc__: Any = ...

class NotAContainer(ValidationError):
    __doc__: Any = ...

class NotAnIterator(ValidationError):
    __doc__: Any = ...

class WrongContainedType(ValidationError):
    __doc__: Any = ...
    errors: Any = ...
    def __init__(self, errors: Optional[Any] = ..., name: Optional[Any] = ..., *args: Any) -> None: ...

class SchemaNotCorrectlyImplemented(WrongContainedType):
    __doc__: Any = ...
    schema_errors: Any = ...
    invariant_errors: Any = ...
    def __init__(self, errors: Optional[Any] = ..., name: Optional[Any] = ..., schema_errors: Optional[Any] = ..., invariant_errors: Any = ..., *args: Any) -> None: ...

class SchemaNotFullyImplemented(ValidationError):
    __doc__: Any = ...

class SchemaNotProvided(ValidationError):
    __doc__: Any = ...
    schema: Any = ...
    value: Any = ...
    def __init__(self, schema: Optional[Any] = ..., value: Optional[Any] = ..., *args: Any) -> None: ...

class NotAnInterface(WrongType, SchemaNotProvided):
    expected_type: Any = ...
    def __init__(self, value: Any, name: Any) -> None: ...

class IFromUnicode(zope.interface.Interface):
    def fromUnicode(value: Any) -> None: ...

class IFromBytes(zope.interface.Interface):
    def fromBytes(value: Any) -> None: ...

class IContextAwareDefaultFactory(zope.interface.Interface):
    def __call__(context: Any) -> None: ...

class IBeforeObjectAssignedEvent(zope.interface.Interface):
    object: Any = ...
    name: Any = ...
    context: Any = ...

class IValidatable(zope.interface.Interface):
    def validate(value: Any) -> None: ...

class NO_VALUE: ...
