import sys
from _collections_abc import dict_keys
from collections.abc import Sequence
from typing import Any

__all__ = ["symtable", "SymbolTable", "Class", "Function", "Symbol"]

def symtable(code: str, filename: str, compile_type: str) -> SymbolTable: ...

class SymbolTable:
    def __init__(self, raw_table: Any, filename: str) -> None: ...
    def get_type(self) -> str: ...
    def get_id(self) -> int: ...
    def get_name(self) -> str: ...
    def get_lineno(self) -> int: ...
    def is_optimized(self) -> bool: ...
    def is_nested(self) -> bool: ...
    def has_children(self) -> bool: ...
    if sys.version_info < (3, 9):
        def has_exec(self) -> bool: ...

    def get_identifiers(self) -> dict_keys[str, int]: ...
    def lookup(self, name: str) -> Symbol: ...
    def get_symbols(self) -> list[Symbol]: ...
    def get_children(self) -> list[SymbolTable]: ...

class Function(SymbolTable):
    def get_parameters(self) -> tuple[str, ...]: ...
    def get_locals(self) -> tuple[str, ...]: ...
    def get_globals(self) -> tuple[str, ...]: ...
    def get_frees(self) -> tuple[str, ...]: ...
    if sys.version_info >= (3, 8):
        def get_nonlocals(self) -> tuple[str, ...]: ...

class Class(SymbolTable):
    def get_methods(self) -> tuple[str, ...]: ...

class Symbol:
    if sys.version_info >= (3, 8):
        def __init__(
            self, name: str, flags: int, namespaces: Sequence[SymbolTable] | None = ..., *, module_scope: bool = ...
        ) -> None: ...
        def is_nonlocal(self) -> bool: ...
    else:
        def __init__(self, name: str, flags: int, namespaces: Sequence[SymbolTable] | None = ...) -> None: ...

    def get_name(self) -> str: ...
    def is_referenced(self) -> bool: ...
    def is_parameter(self) -> bool: ...
    def is_global(self) -> bool: ...
    def is_declared_global(self) -> bool: ...
    def is_local(self) -> bool: ...
    def is_annotated(self) -> bool: ...
    def is_free(self) -> bool: ...
    def is_imported(self) -> bool: ...
    def is_assigned(self) -> bool: ...
    def is_namespace(self) -> bool: ...
    def get_namespaces(self) -> Sequence[SymbolTable]: ...
    def get_namespace(self) -> SymbolTable: ...

class SymbolTableFactory:
    def __init__(self) -> None: ...
    def new(self, table: Any, filename: str) -> SymbolTable: ...
    def __call__(self, table: Any, filename: str) -> SymbolTable: ...
