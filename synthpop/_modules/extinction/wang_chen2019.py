"""
Extinction law from WANG S. and CHEN X. 2019
2019ApJ...877..116W - Astrophys. J., 877, 116-116 (2019/June-1)
The optical to mid-infrared extinction law based on the
APOGEE, Gaia DR2, Pan-STARRS1, SDSS, APASS, 2MASS, and WISE surveys.
"""

__all__ = ['WangChen2019']
__author__ = "J. Klüter"
__date__ = "2022-11-05"
__license__ = "GPLv3"
__version__ = "1.0.0"

from ._extinction import ExtinctionLaw


class WangChen2019(ExtinctionLaw):
    """
    Extinction law from WANG S. and CHEN X. 2019
    2019ApJ...877..116W - Astrophys. J., 877, 116-116 (2019/June-1)
    The optical to mid-infrared extinction law based on the
    APOGEE, Gaia DR2, Pan-STARRS1, SDSS, APASS, 2MASS, and WISE surveys.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.extinction_law_name = 'WangChen2019'

    def Alambda_AV(self, eff_wavelength: float, R_V: float = 3.1) -> float:
        """
        Given an effective wavelength lambda_eff, calculate the relative extinction A_lambda/A_V

        Parameters
        ----------
        eff_wavelength : float
            Effective Wavelength of the filter for which the extinction should be determined.
            in micrometer
        R_V : float
            interstellar reddening parameter

        Returns
        -------
        Al_AV : total extinction relative to the V band  extinction
        """

        x = 1. / wavelength_eff
        if x >= 1.0:
            y = x - 1.82
            Al_AV = (1 + 0.7499 * y - 0.1086 * y ** 2 - 0.08909 * y ** 3 + 0.02905 * y ** 4
                     + 0.01069 * y ** 5 + 0.001707 * y ** 6 - 0.001002 * y ** 7)
        else:
            Al_AV = 0.3722 * x ** 2.07

        return Al_AV
