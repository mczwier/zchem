import matplotlib
import matplotlib.pyplot as plt

pc_per_inch = 6.0

default_aspect_ratio = 16.0/9.0

tuftesque_mainwidth = 26.0/pc_per_inch
tuftesque_sidewidth = 12.0/pc_per_inch

serif_font = 'Minion Pro'
sans_font = 'Optima LT Std'

def mpl_rc_handouts(rc = None):
    if rc is None:
        import matplotlib as mpl
        rc = mpl.rc
    rc('font',**{'family':'serif','serif':[serif_font],'size':9.0})
    rc('axes',**{'labelsize':'medium', 'labelweight':'bold'})
    rc('text', usetex=False)
    rc('figure', figsize=(tuftesque_mainwidth, tuftesque_mainwidth/default_aspect_ratio))
    rc('mathtext', fontset='stix')
    rc('pdf',**{'fonttype': 42})

def mpl_figure_tuftesque_main(aspect_ratio=None):
    '''Set up pyplot figure with appropriate width for use in Tuftesque handouts,
    main column. Height is determined by `aspect_ratio`, which defaults to
    the module variable `default_aspect_ratio`.'''
    if not aspect_ratio:
        aspect_ratio = default_aspect_ratio
    return plt.figure(figsize=(tuftesque_mainwidth, tuftesque_mainwidth/aspect_ratio))
