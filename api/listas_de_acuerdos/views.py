"""
Listas de Acuerdos, vistas
"""
from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from api.autoridades.crud import get_autoridad
from api.listas_de_acuerdos import crud, schemas
from lib.database import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.ListaDeAcuerdo])
async def listar_listas_de_acuerdos(autoridad_id: int, fecha: date = None, ano: int = None, db: Session = Depends(get_db)):
    """ Lista de Listas de Acuerdos """
    autoridad = get_autoridad(db, autoridad_id=autoridad_id)
    if autoridad is None:
        raise HTTPException(status_code=400, detail="No existe la autoridad.")
    resultados = []
    for lista_de_acuerdo, autoridad, distrito in crud.get_listas_de_acuerdos(db, autoridad_id=autoridad_id, fecha=fecha, ano=ano):
        resultados.append(
            schemas.ListaDeAcuerdo(
                id=lista_de_acuerdo.id,
                distrito_id=distrito.id,
                distrito=distrito.nombre,
                autoridad_id=autoridad.id,
                autoridad=autoridad.descripcion,
                fecha=lista_de_acuerdo.fecha,
                descripcion=lista_de_acuerdo.descripcion,
                archivo=lista_de_acuerdo.archivo,
                url=lista_de_acuerdo.url,
            )
        )
    return resultados


@router.get("/{lista_de_acuerdo_id}", response_model=schemas.ListaDeAcuerdo)
async def consultar_una_lista_de_acuerdos(lista_de_acuerdo_id: int, db: Session = Depends(get_db)):
    """ Consultar una Lista de Acuerdos """
    lista_de_acuerdo = crud.get_lista_de_acuerdo(db, lista_de_acuerdo_id=lista_de_acuerdo_id)
    if lista_de_acuerdo is None:
        raise HTTPException(status_code=400, detail="No existe la lista de acuerdos.")
    return schemas.ListaDeAcuerdo(
        id=lista_de_acuerdo.id,
        distrito_id=lista_de_acuerdo.autoridad.distrito_id,
        distrito=lista_de_acuerdo.autoridad.distrito.nombre,
        autoridad_id=lista_de_acuerdo.autoridad_id,
        autoridad=lista_de_acuerdo.autoridad.descripcion,
        fecha=lista_de_acuerdo.fecha,
        descripcion=lista_de_acuerdo.descripcion,
        archivo=lista_de_acuerdo.archivo,
        url=lista_de_acuerdo.url,
    )
