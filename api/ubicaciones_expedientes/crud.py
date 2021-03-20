"""
Ubicaciones de Expedientes, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session

from api.ubicaciones_expedientes.models import UbicacionExpediente
from api.autoridades.models import Autoridad


def get_ubicaciones_expedientes(db: Session, autoridad_id: int = None, expediente: str = None):
    """ Consultar ubicaciones de expedientes """
    consulta = db.query(UbicacionExpediente, Autoridad).join(Autoridad)
    if autoridad_id:
        consulta = consulta.filter(UbicacionExpediente.autoridad_id == autoridad_id)
    if expediente:
        consulta = consulta.filter(UbicacionExpediente.expediente.like(f"%{expediente}%"))
    return consulta.filter(UbicacionExpediente.estatus == "A").order_by(Autoridad.descripcion, UbicacionExpediente.expediente).limit(200).all()


def get_ubicacion_expediente(db: Session, ubicacion_expediente_id: int):
    """ Consultar una ubicacion de expediente """
    return db.query(UbicacionExpediente).get(ubicacion_expediente_id)
