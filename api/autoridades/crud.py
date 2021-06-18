"""
Autoridades, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session

from api.autoridades.models import Autoridad
from api.distritos.models import Distrito


def get_autoridades(db: Session, distrito_id: int = None, con_notarias: bool = False, para_glosas: bool = False):
    """Consultar autoridades"""
    consulta = db.query(Autoridad, Distrito).join(Distrito)
    if distrito_id:
        consulta = consulta.filter(Autoridad.distrito_id == distrito_id)
    if con_notarias is False:
        consulta = consulta.filter(Autoridad.es_notaria == False)
    if para_glosas:
        consulta = consulta.filter(Autoridad.organo_jurisdiccional.in_(["PLENO O SALA DEL TSJ", "TRIBUNAL DISTRITAL"]))
    return consulta.filter(Autoridad.es_jurisdiccional == True).filter(Autoridad.estatus == "A").order_by(Distrito.nombre, Autoridad.clave).all()


def get_autoridad(db: Session, autoridad_id: int):
    """Consultar una autoridad"""
    return db.query(Autoridad).get(autoridad_id)
