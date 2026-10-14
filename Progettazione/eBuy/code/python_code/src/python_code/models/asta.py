from src.python_code.models.datatypes import TimeDelta_GZ
from src.python_code.models.post import Post


class Asta(Post):

  def __init__(self, istante_pubbl: TimeDelta_GZ, durata):...

  # def _scadenza(self):
  #   return istante_pubbl + durata