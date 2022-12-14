# Licensed under a 3-clause BSD style license - see LICENSE.rst
import astropy.units as u
import numpy as np
from gammapy.modeling.models import SpectralModel
from gammapy.modeling import Parameter, Parameters


class SherpaSpectralModel(SpectralModel):
    """A wrapper for Sherpa spectral models.

    Parameters
    ----------
    sherpa_model :
        An instance of the models defined in `~sherpa.models` or `~sherpa.astro.xspec`.
    default_units : tuple
        Units of the input energy array and output model evaluation (find them in the sherpa/xspec docs!)
    """

    tag = ["SherpaSpectralModel", "sherpa", "xspec"]

    def __init__(
        self, sherpa_model, integrated=True, default_units=(u.keV, 1 / (u.keV * u.cm ** 2 * u.s))
    ):
        self.sherpa_model = sherpa_model
        self.default_units = default_units
        self.default_parameters = self._wrap_parameters()
        self.integrated = integrated
        super().__init__()

    def _wrap_parameters(self):
        parameters = []
        for par in self.sherpa_model.pars:
            is_norm = par.name in ["ampl", "norm", "K"]
            parameter = Parameter(
                name=par.name, value=par.val, frozen=par.frozen, min=par.min, max=par.max, is_norm=is_norm
            )
            # TODO: set unit?
            parameters.append(parameter)
        return Parameters(parameters)

    def _update_sherpa_parameters(self, **kwargs):
        """Update sherpa model parameters"""
        for name, value in kwargs.items():
            setattr(self.sherpa_model, name, value)

    def evaluate(self, energy, **kwargs):
        if not isinstance(energy, u.Quantity):
            raise ValueError("The energy must be a Quantity object.")
        else:
            energy = energy.to(self.default_units[0])

        # Trickeries due to the sherpa model evaluation scheme
        # (https://sherpa.readthedocs.io/en/4.14.1/evaluation/index.html)
        energy = np.array(energy, dtype=float)
        shape = energy.shape
        energy = energy.flatten()
        energy = np.append(energy, energy[-1] * 2)

        # Remove duplicate energies by adding a negligible value
        # (otherwise there are problems with some models, e.g. wabs)
        for idx in range(len(energy) - 1):
            if energy[idx] == energy[idx + 1]:
                delta = (energy[idx + 2] - energy[idx + 1]) / 100
                energy[idx + 1] += delta

        self._update_sherpa_parameters(**kwargs)

        y_ = self.sherpa_model(energy)[:-1]
        if self.integrated:
            y_ /= energy[1:] - energy[:-1]
        y_ = y_ * self.default_units[1]

        return y_.reshape(shape)
