import os

#1 WAY - TypedDict

from typing import TypedDict

class State(TypedDict):
    topic:str
    summary: str
    score:int

#2 WAY - Pydantic Model

from pydantic import BaseModel,field_validator

class State(BaseModel):
    topic: str
    score:int
    summary:str = ""

    @field_validator
    def score_positive(cls,v):
        if v < 0:
            raise ValueError("score must be positive")
             

from langgraph.graph import MessagesState

class State(MessagesState):
    user_name:str
    language:str