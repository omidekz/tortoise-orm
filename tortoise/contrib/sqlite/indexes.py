from typing import Sequence
from tortoise.indexes import UniqueIndexABC


class UniqueIndex(UniqueIndexABC[Sequence[str]]):
    def nulls(self, null_fields: Sequence[str]):
        conditions = tuple(
            map(
                lambda field_name: f"{field_name} is not null",
                null_fields or [],
            )
        )
        result = " and ".join(conditions)
        return f"where {result}" if result else result
