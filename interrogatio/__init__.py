from .core import interrogatio
from .enums import Mode

__version__ = '1.0.0b2'

__version_info__ = tuple([int(num) if num.isdigit() else num for num in __version__.replace('-', '.', 1).split('.')])


def get_version():
    return __version__
