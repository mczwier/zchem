import numpy as np

def read_xvg(filename, *args, **kwargs):
    '''A little function to read a GROMACS-produced XVG file, automatically
    skipping over the default xmgr formatting. `args` and `kwargs`
    are passed along to `numpy.loadtxt`'''

    skiprows = 0
    with open(filename, 'rt') as xvgfile:
        for line in xvgfile:
            if line[0] in ('#', '@'):
                skiprows += 1
                continue
            else:
                break
    return np.loadtxt(filename, skiprows=skiprows, *args, **kwargs)
