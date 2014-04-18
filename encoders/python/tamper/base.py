# -*- coding: utf-8 -*-

'''

  tamper for python: base classes

'''

# stdlib
import abc


## Globals
_pack_strategies = {}


class BasePack(object):

  '''  '''

  __slots__ = (
    '__name__',
    '__possibilities__',
    '__max_choices__',
    '__encoding__',
    '__bitset__',
    '__bit_window_width__',
    '__max_guid__',
    '__meta__'
  )

  __metaclass__ = abc.ABCMeta

  def __init__(name, possibilities, max_choices):

    '''  '''

    self.__meta__ = {}  # initialize meta

    # initialize name, possibilities & max choices
    self.__name__, self.__possibilities__, self.__max_choices__ = (
      name, possibilities, max_choices
    )

    if not possibilities:
      raise ValueError('Empty possibilities passed for attr "%s".' % name)

  @classmethod
  def _bind(cls, name):

    '''  '''

    return setattr(cls, '__encoding__', name) or cls

  def _build(self, name, possibilities, max_choices):

    '''  '''

    pass

  @abc.abstractproperty
  def header(self):

    '''  '''

    raise NotImplementedError('`BasePack.header` is abstract and cannot be'
                              ' accessed directly.')

  @abc.abstractmethod
  def initialize(self, max_guid, num_items):

    '''  '''

    raise NotImplementedError('`BasePack.initialize` is abstract and cannot'
                              ' be invoked directly.')

  @abc.abstractmethod
  def encode(self, idx, data):

    '''  '''

    raise NotImplementedError('`BasePack.encode` is abstract and cannot be'
                              ' invoked directly.')

  @abc.abstractmethod
  def finalize(self):

    '''  '''

    raise NotImplementedError('`BasePack.finalize` is abstract and cannot'
                              ' be invoked directly.')

  ## == Properties == ##
  name = property(lambda self: self.__name__)
  possibilities = property(lambda self: self.__possibilities__)
  max_choices = property(lambda self: self.__max_choices__)
  encoding = property(lambda self: self.__encoding__)
  bitset = property(lambda self: self.__bitset__)
  bit_window_width = property(lambda self: self.__bit_window_width__)
  max_guid = property(lambda self: self.__max_guid__)
  meta = property(lambda self: self.__meta__)


class Pack(BasePack):

  '''  '''

  @property
  def header(self):

    '''  '''

    pass

  def finalize(self):

    '''  '''

    pass

  @classmethod
  def bind(cls, name):

    '''  '''

    global _pack_strategies

    def _bind_pack(target):

      '''  '''

      _pack_strategies[name] = target._bind(name)
      return target

    return _bind_pack
