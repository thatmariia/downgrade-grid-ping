from src.misc import *

class PINGNetworkPixels:
    """
    This class contains information about a single stimulus patch-related information about a PING network.

    :param center: coordinates of the center of the PING network within the stimulus patch.
    :type center: tuple[float, float]

    :param pixels: list of pixel coordinates that belong to the PING network.
    :type pixels: list[tuple[int, int]]

    :param atopix: conversion coefficient between pixels and visual degrees.
    :type atopix: float

    :param grid_location: index of the PING network in the grid.
    :type grid_location: tuple[int, int]


    :ivar center: coordinates of the center of the PING network within the stimulus patch (in pixels).
    :ivar pixels: list of coordinates that belong to the PING network (in pixels).
    :ivar center: coordinates of the center of the PING network within the stimulus patch (in degrees).
    :ivar pixels: list of pixel coordinates that belong to the PING network (in degrees).
    :ivar grid_location: index of the PING network in the grid.
    """

    def __init__(
            self,
            center, pixels, atopix: float, grid_location
    ):
        self.center = center
        self.pixels = pixels

        self.center_dg = multiply_point(center, 1 / atopix)
        self.pixels_dg = [multiply_point(p, 1 / atopix) for p in pixels]

        self.grid_location = grid_location
