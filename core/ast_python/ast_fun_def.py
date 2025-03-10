import ast
from typing import Any


class AstFuncDefObj:
    @staticmethod
    def create_function(
        name: str,
        args: ast.arguments | None = None,
        body: list[Any] | None = None,
        decorator_list: Any | None = None,
    ):
        return ast.FunctionDef(
            name=name,
            args=args if args is not None else [],
            body=body if body is not None else [],
            decorator_list=decorator_list if decorator_list is not None else [],
        )

    @staticmethod
    def create_function_alfa(
        name: str,
        in_args: dict[str, str | None] | None = None,
        in_args_defaults_list: dict[str, str | None] | None = None,
        body: list[Any] | None = None,
        decorator_list: Any | None = None,
    ):
        return ast.FunctionDef(
            name=name,
            args=AstSimpleObj.arguments_(
                AstSimpleObj.arg_alfa(in_args), in_args_defaults_list
            )
            if in_args is not None
            else [],
            body=body if body is not None else [],
            decorator_list=decorator_list if decorator_list is not None else [],
        )

    @staticmethod
    def create_arguments_function(
        posonlyargs: list[ast] | None = None,
        args: list[ast] | None = None,
        kwonlyargs: list[ast] | None = None,
        kw_defaults: list[ast] | None = None,
        defaults: list[ast] | None = None,
    ):
        return ast.arguments(
            posonlyargs=posonlyargs if posonlyargs is not None else [],
            args=args if args is args is not None else [],
            kwonlyargs=kwonlyargs if kwonlyargs is not None else [],
            kw_defaults=kw_defaults if kw_defaults is not None else [],
            defaults=defaults if defaults is not None else [],
        )

    @staticmethod
    def create_bode_function(
        list_body,
    ) -> list[ast.Assign, ast.Expr, ast.Return] | list[None]:
        return [b for b in list_body]
