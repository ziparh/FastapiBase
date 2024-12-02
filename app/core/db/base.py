from sqlalchemy.orm import DeclarativeBase, declared_attr
from app.utils.case_conventer import camel_case_to_snake_case

class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{camel_case_to_snake_case(cls.__name__)}s'
