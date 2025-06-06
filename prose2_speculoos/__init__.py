import warnings
from astropy.wcs import FITSFixedWarning

warnings.simplefilter("ignore", FITSFixedWarning)

from . import config

CONFIG = config.ConfigManager()
CONFIG.check_builtins_changes()

from . import visualization as viz

from .io.fitsmanager import FitsManager
from .fluxes import ApertureFluxes
from .telescope import Telescope
from .block import Block
from .sequence import Sequence
from .image import Image
from .observation import Observation
from .observations import Observations

#from pkg_resources import get_distribution
#__version__ = get_distribution('prose').version
