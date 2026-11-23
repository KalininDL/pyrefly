"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

import dataclasses
from collections.abc import Callable


@dataclasses.dataclass(slots=True)
class AliasPath:
    path: list[int | str]

    def __init__(self, first_arg: str, *args: str | int) -> None: ...


@dataclasses.dataclass(slots=True)
class AliasChoices:
    choices: list[str | AliasPath]

    def __init__(
        self, first_choice: str | AliasPath, *choices: str | AliasPath
    ) -> None: ...


@dataclasses.dataclass(slots=True)
class AliasGenerator:
    alias: Callable[[str], str] | None = None
    validation_alias: Callable[[str], str | AliasPath | AliasChoices] | None = None
    serialization_alias: Callable[[str], str] | None = None
