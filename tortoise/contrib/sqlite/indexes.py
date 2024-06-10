from typing import Sequence
from tortoise.indexes import UniqueIndexABC


class SqliteUniqueIndex(UniqueIndexABC[Sequence[str]]):

    @staticmethod
    def get_conditions(fields: Sequence[str]):
        conditions = tuple(
            map(
                lambda field_name: f"{field_name} is not null",
                fields or [],
            )
        )
        return " and ".join(conditions)

    def nulls(self, null_fields: Sequence[str]):
        result = self.get_conditions(null_fields)
        return f"where {result}" if result else result
