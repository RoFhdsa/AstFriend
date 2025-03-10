import ast
from enum import Enum


class TypeKeyWords (str, Enum):
    list_ = "list"
    str_ = "str"
    none_ = "None"

class ClassKeyWords:
    "Класс со стандратными объектами в формате ast и текстом"
    init_ = "__init__"
    super_ = "super"
    classmethod_ = "classmethod"
    super_name = ast.Name(id="super", ctx=ast.Load())
    self_ = "self"
    self_name = ast.Name(id="self", ctx=ast.Load())
    self_arg = ast.arg(arg="self", annotation=None)
    cls_ = "cls"
    cls_arg = ast.arg(arg="cls", annotation=None)


class AnnotationKeyWords:
    "Класс со стандратными типами python в формате ast.name"
    list_: ast.Name = ast.Name(id="list", ctx=ast.Load())
    str_: ast.Name = ast.Name(id="str", ctx=ast.Load())
    callable_: ast.Name = ast.Name(id="callable", ctx=ast.Load())
    dict_: ast.Name = ast.Name(id="dict", ctx=ast.Load())
    none_: ast.Name = ast.Name(id="None", ctx=ast.Load())