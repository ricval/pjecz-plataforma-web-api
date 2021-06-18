"""
Edictos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import date
from sqlalchemy.orm import Session

from api.edictos.models import Edicto
from api.autoridades.models import Autoridad
from api.distritos.models import Distrito


def get_edictos(db: Session, autoridad_id: int = None, ano: int = None):
    """Consultar edictos"""
    edictos = db.query(Edicto, Autoridad, Distrito).select_from(Edicto).join(Autoridad).join(Distrito)
    if autoridad_id:
        edictos = edictos.filter(Edicto.autoridad_id == autoridad_id)
    if ano and ano >= 2000 and ano <= date.today().year:
        edictos = edictos.filter(Edicto.fecha >= date(ano, 1, 1)).filter(Edicto.fecha <= date(ano, 12, 31))
    return edictos.filter(Edicto.estatus == "A").order_by(Edicto.fecha.desc()).limit(500).all()


def get_edicto(db: Session, edicto_id: int):
    """Consulta un edicto"""
    return db.query(Edicto).get(edicto_id)
