import numpy as np
from scipy.optimize import curve_fit

class Model:
    def __init__(self):
        self._params = None
        self.param_names = None

    def _set_params(self, params):
        self._params = np.array(params)
        if self.param_names is None:
            self.param_names = ['param{:d}'.format(i) for i,p in enumerate(self._params)]

    def _get_params(self):
        return self._params

    params = property(_get_params, _set_params, None)

    def fit(self, x, y):
        new_params, covar_matrix = curve_fit(self, x, y, self._get_params())
        self.init_params = self.params
        self._set_params(new_params)

class GaussianModel(Model):

    param_names = ('center', 'amplitude', 'width')

    def __init__(self, center, amplitude, width):
        self._set_params([center, amplitude, width])

    def __call__(self, x):
        params = self.params
        center = params[0]
        amplitude = params[1]
        width = params[2]
        return amplitude * np.exp(-((x - center)/width)**2/2)

class LorentzianModel(Model):
    param_names = ('center', 'amplitude', 'width')

    def __init__(self, center, amplitude, width):
        self._set_params([center, amplitude, width])

    def __call__(self, x):
        params = self.params
        center = params[0]
        amplitude = params[1]
        width = params[2]

        nx = 2*(center-x)/(width)

        return amplitude/(1+nx**2)

class CompoundModel(Model):
    def __init__(self, models):
        self.models = list(models)

class SumModel(CompoundModel):

    def _set_params(self, params):
        iargs = 0
        for model in self.models:
            nargs = len(model.params)
            model.params = params[iargs:iargs+nargs]
            iargs += nargs

    def _get_params(self):
        params = []
        for model in self.models:
            params.extend(model._get_params())
        return params

    params = property(_get_params, _set_params)

    def __call__(self, x):
        if np.isscalar(x):
            result = 0
        else:
            result = np.zeros_like(x)

        for model in self.models:
            result += model(x)
        return result
