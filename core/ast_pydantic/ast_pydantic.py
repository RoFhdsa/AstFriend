import ast

from core.ast_python.ast_class_def import AstClassDefObj
from core.objs.keywords.pydantic_keywords import PydanticKeyWords


class AstCreateBaseModel:
    @staticmethod
    def create_class_standart_padantic_model(
        class_name: str,
        body: list[ast],
        bases: list[ast.Name] = AstClassDefObj.get_basses(
            [PydanticKeyWords.base_model_]
        ),
    ) -> ast.ClassDef:
        return ast.ClassDef(
            name=class_name,
            bases=bases,
            keywords=[],
            body=body,
            decorator_list=[],
        )

    @staticmethod
    def get_class_model_dump(name_model: str) -> ast.Call:
        """name_model().model_dump(by_alias=True)"""
        return AstSimpleObj.call_alfa(
            func_=AstSimpleObj.attribute_value(
                value_=AstSimpleObj.call_(func_=AstSimpleObj.name_(name_model)),
                attr_="model_dump",
            ),
            keywords_=[{"by_alias": ast.NameConstant(value=True)}],
        )

    @staticmethod
    def get_class_model_dump_not_call(name_model: str) -> ast.Call:
        """name_model.model_dump(by_alias=True)"""
        return AstSimpleObj.attribute_value(
            value_=AstSimpleObj.name_(name_model),
            attr_="model_dump(by_alias=True)",
        )

    @staticmethod
    def create_name_attribute(prop_name: str) -> CorrectName:
        name_change = (
            prop_name if prop_name.islower() else camel_to_snake_lower_mz(prop_name)
        )
        name_change = change_keyword_name(name_change)
        alias = (
            prop_name
            if not prop_name.islower() or name_change != prop_name
            else prop_name
        )
        return CorrectName(name_change, alias)

    @staticmethod
    def create_attribute_standard_pydantic_model(
        field_name: str,
        field_type: str,
        is_nullable: bool = False,
        alias: str | None = None,
        description: str | None = None,
    ) -> ast.AnnAssign:
        """
        :param field_name: имя поля в модели или атрибута модели
        :param field_type: тип данных для данного атрибута
        :param is_nullable: может ли быть пустым
        :param alias: синоним для имени, если имя не в snake_case или имя зарезервировано python
        :return:
        """
        return ast.AnnAssign(
            target=ast.Name(id=field_name, ctx=ast.Store()),
            annotation=ast.Name(
                id=f"{field_type} | {TypeKeyWords.none_}", ctx=ast.Store()
            )
            if is_nullable
            else ast.Name(id=f"{field_type}", ctx=ast.Store()),
            value=ast.Call(
                func=ast.Name(id=PydanticKeyWords.field_, ctx=ast.Load()),
                args=[ast.Constant(value=None)] if is_nullable else [],
                keywords=[
                    *(
                        [
                            ast.keyword(
                                arg=PydanticKeyWords.alias_,
                                value=ast.Constant(value=alias),
                            )
                        ]
                        if alias
                        else []
                    ),
                    *(
                        [
                            ast.keyword(
                                arg="description", value=ast.Constant(value=description)
                            )
                        ]
                        if description
                        else []
                    ),
                ],
            )
            if alias
            else (AnnotationKeyWords.none_ if is_nullable else None),
            simple=1,
        )
