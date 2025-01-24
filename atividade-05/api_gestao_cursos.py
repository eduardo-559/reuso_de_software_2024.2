from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modelo de Curso
class Curso(BaseModel):
    titulo: str
    descricao: str
    carga_horaria: int

# Banco de dados em memória
banco_cursos = {}
id_counter = 1

# Endpoints

@app.get("/cursos", response_model=List[Curso])
def listar_cursos():
    return list(banco_cursos.values())

@app.get("/cursos/{id}", response_model=Curso)
def obter_curso(id: int):
    curso = banco_cursos.get(id)
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso

@app.post("/cursos", response_model=Curso)
def criar_curso(curso: Curso):
    global id_counter
    curso_id = id_counter
    banco_cursos[curso_id] = curso
    id_counter += 1
    return curso

@app.put("/cursos/{id}", response_model=Curso)
def atualizar_curso(id: int, curso_atualizado: Curso):
    if id not in banco_cursos:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    banco_cursos[id] = curso_atualizado
    return curso_atualizado

@app.delete("/cursos/{id}", response_model=dict)
def excluir_curso(id: int):
    if id not in banco_cursos:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    del banco_cursos[id]
    return {"message": "Curso excluído com sucesso"}
