# -*- coding: utf-8 -*-

'''

  tamper for python: existence pack

'''

# base pack class
from ..base import Pack


@Pack.bind('existence')
class ExistencePack(Pack):

  '''  '''

  __slots__ = (
    '__output__',
    '__current_chunk__',
    '__last_guid__',
    '__run_counter__'
  )

  ## == Internals == ##
  def _dump_keep(self, chunk, run_len):

    '''  '''

    pass

  def _control_code(self, command, offset=0):

    '''  '''

    pass

  ## == Public == ##
  @property
  def header(self):

    '''  '''

    return {

    }

  def initialize(self, max_guid, num_items):

    '''  '''

    pass

  def encode(self, guid):

    '''  '''

    pass

  def finalize(self):

    '''  '''

    pass
