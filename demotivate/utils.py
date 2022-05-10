from typing_extensions import TypeAlias


Color: TypeAlias = int | str | tuple[int, int, int] | tuple[int, int, int, int]
Indent: TypeAlias = tuple[int, int, int, int]
Number: TypeAlias = int | float
Position: TypeAlias = tuple[int, int]
