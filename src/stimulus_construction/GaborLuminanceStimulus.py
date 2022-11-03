from src.misc import *

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class GaborLuminanceStimulus:
    """
    This class contains information about the full stimulus and a patch.

    :param atopix: conversion coefficient between pixels and visual degrees.
    :type atopix: float

    :param stimulus: luminance matrix of the stimulus.
    :type stimulus: numpy.ndarray[(int, int), float]

    :param stimulus_center: the center of the full stimulus.
    :type stimulus_center: tuple[float, float]

    :param stimulus_patch: the luminance matrix of a patch of the stimulus.
    :type stimulus_patch: numpy.ndarray[(int, int), float]

    :param patch_start: top left coordinate of the patch.
    :type patch_start: tuple[int, int]


    :ivar atopix: conversion coefficient between pixels and visual degrees.
    :ivar stimulus: luminance matrix of the stimulus.
    :ivar stimulus_center: the center of the full stimulus.
    :ivar stimulus_patch: the luminance matrix of a patch of the stimulus.
    :ivar patch_start: top left coordinate of the patch.
    """

    def __init__(
            self,
            atopix: float,
            stimulus,
            stimulus_center,
            stimulus_patch,
            patch_start
    ):
        self.atopix: float = atopix
        self.stimulus = stimulus
        self.stimulus_center = stimulus_center
        self.stimulus_patch = stimulus_patch
        self.patch_start = patch_start


