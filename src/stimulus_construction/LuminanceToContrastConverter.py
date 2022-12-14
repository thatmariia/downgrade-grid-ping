from src.params.ParamsReceptiveField import *

from src.stimulus_construction.PatchGeometry import *
from src.stimulus_construction.GaborLuminanceStimulus import *

import numpy as np
from math import sqrt, exp
from statistics import mean
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm


class LuminanceToContrastConverter:
    """
    This class converts the luminance stimulus into the local contrasts stimulus.
    """

    def convert(
            self,
            params_rf: ParamsReceptiveField, patch_geometry: PatchGeometry, stimulus_luminance: GaborLuminanceStimulus
    ):
        """
        Converts the luminance stimulus into the local contrasts stimulus.

        The approach is derived from :cite:p:`MaryamPLACEHOLDER`.

        :param params_rf: parameters for the receptive field.
        :type params_rf: ParamsReceptiveField

        :param patch_geometry: information about the grid layout of the stimulus patch in correspondence with PING networks.
        :type patch_geometry: PatchGeometry

        :param stimulus_luminance: luminance stimulus container.
        :type stimulus_luminance: GaborLuminanceStimulus

        :return: the stimulus converted to local contrasts.
        :rtype: numpy.ndarray[int, float]
        """

        return self._compute_local_contrasts(params_rf, patch_geometry, stimulus_luminance)

    def _compute_local_contrasts(
            self,
            params_rf: ParamsReceptiveField, patch_geometry: PatchGeometry, stimulus_luminance: GaborLuminanceStimulus
    ):
        """
        Computes local contrasts for each circuit.

        :param patch_geometry: information about the grid layout of the stimulus patch in correspondence with PING networks.
        :type patch_geometry: PatchGeometry

        :param stimulus_luminance: luminance stimulus container.
        :type stimulus_luminance: GaborLuminanceStimulus

        :param params_rf: parameters for the receptive field.
        :type params_rf: ParamsReceptiveField

        :return: list containing local contrast values for each circuit.
        :rtype: numpy.ndarray[int, float]
        """

        # TODO:: optimize

        mean_luminance = mean(np.array(stimulus_luminance.stimulus).flatten())
        local_contrasts = []

        for curr_circuit in (pbar := tqdm(patch_geometry.ping_networks_pixels)):
            pbar.set_description("Local contrast computation")

            eccentricity = patch_geometry.eccentricity_in_patch(point=curr_circuit.center_dg)
            num = 0
            denum = 0

            for circuit in patch_geometry.ping_networks_pixels:
                for i in range(len(circuit.pixels)):
                    pix = circuit.pixels[i]
                    pix_dg = circuit.pixels_dg[i]

                    weight = self._get_weight(
                        center=curr_circuit.center_dg,
                        pixel=pix_dg,
                        eccentricity=eccentricity,
                        params_rf=params_rf
                    )

                    num += weight * (stimulus_luminance.stimulus_patch[pix[0]][pix[1]] - mean_luminance) ** 2 / (mean_luminance ** 2)
                    denum += weight

            local_contrast = sqrt(num / denum)
            local_contrasts.append(local_contrast)

        return np.array(local_contrasts)

    def _get_weight(
            self,
            center, pixel, eccentricity: float,
            params_rf: ParamsReceptiveField
    ) -> float:
        """
        Computes weight of a pixel with respect to a circuit.

        :param center: coordinate of the circuit center.
        :type center: tuple[float, float]

        :param pixel: coordinate of the pixel.
        :type pixel: tuple[float, float]

        :param eccentricity: eccentricity of the circuit center.
        :type eccentricity: float

        :param params_rf: parameters for the receptive field.
        :type params_rf: ParamsReceptiveField

        :return: weight of a pixel with respect to a circuit.
        :rtype: float
        """

        diam_rf = max(params_rf.slope * eccentricity + params_rf.intercept, params_rf.min_diam_rf)
        std = diam_rf / 4.0
        return exp(-(euclidian_dist(pixel, center) ** 2) / (2 * std ** 2))
