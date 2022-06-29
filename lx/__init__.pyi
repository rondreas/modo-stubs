""" Module for modo extensions. """

from typing import Optional, Any

from . import ifc
from . import object
from . import result
from . import service
from . import symbol


class Monitor(object):
    def __init__(self, count: Optional[int]):
        ...

    def init(self, count: int):
        """Initialize the monitor with the total number of steps"""
        ...

    def step(self, count: int):
        """Increment the monitor by one or by step it by an arbitrary amount"""
        ...


class Service(object):
    def name(self):
        """Return the name of the script service."""
        ...

    def query(self):
        """Query an attribute from the selection."""
        ...

    def query1(self):
        """Query an attribute from the selection, returning a single value."""
        ...

    def queryN(self):
        """Query an attribute from the selection, returning a tuple."""
        ...

    def select(self, element):
        """Select a an attribute (and element) for query."""
        ...


def arg() -> str:
    """Get the argument string for the script."""
    ...


def args() -> tuple:
    """Get the parsed argument tuple for the script."""
    ...


def bless(cls: type, name: str, tags: Optional[dict] = None, meta: Optional[Any] = None):
    """ Export a class as a server object:

        lx.bless(cls, name, [tags, meta])

          cls   - class to bless
          name  - the server name
          tags  - optional dictionary of server tags
          meta  - optional metaclass object

    The class must be derived in part from lxifc base classes, and the first
    class in the hierarchy is the server type. The name must be unique for all
    servers of this same type in the system. Tags are given by a dictionary of
    tag[key] = value pairs. The metaclass is ...ed as argument to the
    __init__() method, providing global state to customize the class.

    """
    ...


def command(*args, **kwargs):
    """ Execute a command with a variable argument list."""
    ...


def eval(expression: str) -> Any | None:
    """ Evaluate a command string."""
    ...


def eval1(expression: str) -> Any:
    """ Evaluate a command string, returning a single value."""
    ...


def evalN(expression: str) -> tuple:
    """ Evaluate a command string, returning a tuple."""
    ...


def excResult(exception: Exception) -> int:
    """ Get the exception as an LxResult code."""
    ...


def extract():
    """ Extract the Python object referenced from a COM object wrapper."""
    ...


def getQWidget():
    """ Converts a PyLong object to a PySide QWidget"""
    ...


def lastResult() -> int:
    """ Get the result code from the last service or object method called."""
    ...


def notimpl():
    """ Raise 'not implemented' exception."""
    ...


def option():
    """ Get the current state of an option"""
    ...


def out(message: str):
    """ Output to log."""
    ...


def outEx():
    """ Output the exception state to the log."""
    ...


def queryToggle():
    """ Query a command with a ToggleValue style argument."""
    ...


def setOption():
    """ Set options that affect how the lx methods act"""
    ...


def test():
    """ Test the state of a toggle argument."""
    ...


def testifc():
    """ Test an interface GUID against a class:

        ok = lx.testifc(cls, guid, [meta])"""
    ...


def throw(code: int, quiet: Optional[bool]):
    """ Raise a result code exception.

       lx.throw(code, [quiet])"""
    ...


def trace():
    """ Toggle extra Event Log output for each lx function call."""
    ...

