from scipy import constants as spc
from . import conversions as zc

MJPERMOL_PER_EV = 1.0 / 10.3642696563

kB_Eh = spc.k / zc.J_per_Hartree
kB_wavenumbers = spc.k / zc.J_per_eV * zc.wavenumbers_per_eV
