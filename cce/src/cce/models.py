from __future__ import annotations

from pydantic import BaseModel, Field


class Node(BaseModel):
    name: str
    memory: list[str] = Field(default_factory=list)


class Relationship(BaseModel):
    source: Node
    relation: str
    target: Node


class Memory(BaseModel):
    nodes: list[Node] = Field(default_factory=list)
    relationships: list[Relationship] = Field(default_factory=list)

