# This file is auto-generated by build/generate_typehints.py
from __future__ import annotations
from typing import Literal, TypedDict


class ClickParam(TypedDict):
    click1: str


class CommonParam(TypedDict):
    common1: str
    common10: str
    common11: str
    common12: str
    common13: str
    common14: str
    common15: str
    common16: str
    common2: str
    common3: str
    common4: str
    common5: str
    common6: str
    common7: str
    common8: str
    common9: str


class DragParam(TypedDict):
    drag1: str


class EatParam(TypedDict):
    eat1: str


class HungryParam(TypedDict):
    hungry1: str


class MoveParam(TypedDict):
    move1: str
    move2: str
    move3: str
    move4: str
    move5: str
    move6: str
    move7: str


class GifDirParam(TypedDict):
    Click: ClickParam
    Common: CommonParam
    Drag: DragParam
    Eat: EatParam
    Hungry: HungryParam
    Move: MoveParam


GifDirLiteral = Literal["Click", "Common", "Drag", "Eat", "Hungry", "Move"]
ClickLiteral = Literal["click1"]
CommonLiteral = Literal[
    "common1",
    "common10",
    "common11",
    "common12",
    "common13",
    "common14",
    "common15",
    "common16",
    "common2",
    "common3",
    "common4",
    "common5",
    "common6",
    "common7",
    "common8",
    "common9",
]
DragLiteral = Literal["drag1"]
EatLiteral = Literal["eat1"]
HungryLiteral = Literal["hungry1"]
MoveLiteral = Literal["move1", "move2", "move3", "move4", "move5", "move6", "move7"]
GifDirParamLiteral = Literal[
    ClickParam, CommonParam, DragParam, EatParam, HungryParam, MoveParam
]
