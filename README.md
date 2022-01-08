# Simple TODO API with python and FastApi

A simple TODO API, to understand the concepts of the Library FastApi, and how we can use the `pydantic` and `typing` library, to create a class and define the type of each variable. View the example below:
```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ToDo(BaseModel):
    tarefa: str # type str
    realizada: bool # type bool
    prazo: Optional[datetime] # optional parameter with datetime type
```