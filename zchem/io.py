import numpy as np

def read_xyz(infile):
    n_atoms = int(infile.readline().strip())
    title = infile.readline().strip()

    atoms = [None]*n_atoms
    coords = np.empty((n_atoms,3), dtype=np.float64)

    for i in range(n_atoms):
        line = infile.readline()
        fields = line.split()
        atoms[i] = fields[0]
        coords[i,0] = float(fields[1])
        coords[i,1] = float(fields[2])
        coords[i,2] = float(fields[3])

    return atoms, coords

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
