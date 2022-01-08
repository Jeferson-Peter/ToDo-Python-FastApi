from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()

class ToDo(BaseModel):
    tarefa: str
    realizada: bool
    prazo: Optional[datetime]

lista = []

@app.post("/inserir")
def inserir(todo: ToDo):
    try:
        lista.append(todo)
        return {'status': 'sucesso'}
    except:
        return {'status': 'error'}

@app.post("/listar")
def listar(opcao: int = 0):
    if opcao == 0:
        return lista
    elif opcao == 1:
        return list(filter(lambda x: x.realizada == False, lista))
    elif opcao == 2:
        return list(filter(lambda x: x.realizada == True, lista))

@app.get("/listar/{id}")
def listar( id : int):
    try:
        return lista[id]
    except:
        return {'status':'error'}

@app.put('/alterar/{id}')
def alterar(id: int):
    try:
        lista[id].realizada = not lista[id].realizada
        return {'status':'successo'}
    except:
        return {'status':'error'}

app.delete('/deletar/{id}')
def deletar(id: int):
    try:
        del lista[id]
        return {'status':'successo'}
    except:
        return {'status':'error'}