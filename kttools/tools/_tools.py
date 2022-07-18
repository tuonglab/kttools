#!/usr/bin/env python
# @Author: kt16
# @Date:   2020-07-30 12:52:55
# @Last Modified by:   Kelvin
# @Last Modified time: 2022-07-18 11:40:08
"""Miscellaneous functions."""
import numpy as np

from matplotlib import cm
from matplotlib.colors import ListedColormap
from numpy import ndarray

from typing import Optional, List, Dict, Tuple


def cmp(palette: str = "viridis") -> ListedColormap:
    """
    Create a cmap palette with grey as the first colour.

    Parameters
    ----------
    palette : str, optional
        Accepts palette accepted by `matplotlib.cm.get_cmap`.

    Returns
    -------
    ListedColormap
        ListedColormap instance with grey as the first colour.
    """
    viridis = cm.get_cmap(palette, 256)
    newcolors = viridis(np.linspace(0, 1, 256))
    grey = np.array([215 / 256, 215 / 256, 215 / 256, 1])
    newcolors[:1, :] = grey
    newcmp = ListedColormap(newcolors)
    return newcmp


def get_hex(pal: str, n: Optional[int] = None) -> List:
    """
    Convert rgb colour code to hex code.

    Parameters
    ----------
    pal : str
        Accepts palette accepted by `matplotlib.cm.get_cmap`.
    n : Optional[int], optional
        Number of colours to return.

    Returns
    -------
    List
        List of hex colours.
    """
    if n is None:
        n = 5
    else:
        n = n
    cmap = cm.get_cmap(pal, n)  # PiYG

    cols = []
    for i in range(cmap.N):
        rgba = cmap(i)  # rgb2hex accepts rgb or rgba
        cols.append(matplotlib.colors.rgb2hex(rgba))
    return cols


def colorRampPalette(
    low: str, high: str, diverging: bool = False, medium: str = None, n: int = None
):
    """
    Python implementation of R's colorRampPalette.

    Parameters
    ----------
    low : str
        colour key for low value.
    high : str
        colour key for high value.
    diverging : bool, optional
        diverging palette or not
    medium : str, optional
        colour key for middle value.
    n : int, optional
        number or colours to return in spectrum.

    No Longer Returned
    ------------------
    TYPE
    Description
    """
    if medium is None:
        medium_ = "#FFFFFF"

    if n is None:
        n_ = 256
    else:
        n_ = n

    def hex_to_RGB(hex: str) -> List:
        """
        Convert hex code to rgb code.

        e.g. "#FFFFFF" -> [255,255,255]

        Parameters
        ----------
        hex : str
            colour hex code.

        Returns
        -------
        List
            colour rgb code.
        """
        # Pass 16 to the integer function for change of base
        return [int(hex[i : i + 2], 16) for i in range(1, 6, 2)]

    def RGB_to_hex(RGB: List) -> str:
        """
        Convert rgb code to hex code.

        [255,255,255] -> "#FFFFFF"

        Parameters
        ----------
        RGB : List
            colour rgb code.

        Returns
        -------
        str
            colour hex code.

        """
        # Components need to be integers for hex to make sense
        if len(RGB) == 4:
            RGB = [int(x) for x in RGB[:3]]
        else:
            RGB = [int(x) for x in RGB]
        return "#" + "".join(
            ["0{0:x}".format(v) if v < 16 else "{0:x}".format(v) for v in RGB]
        )

    def color_dict(gradient: List) -> Dict:
        """
        Create dictionary of colours.

        Takes in a list of RGB sub-lists and returns dictionary of
        colors in RGB and hex form for use in a graphing function
        defined later on

        Parameters
        ----------
        gradient : List
            list of rgb codes.

        Returns
        -------
        Dict
            Dictionary of hex, r, g and b colour codes.
        """
        return {
            "hex": [RGB_to_hex(RGB) for RGB in gradient],
            "r": [RGB[0] for RGB in gradient],
            "g": [RGB[1] for RGB in gradient],
            "b": [RGB[2] for RGB in gradient],
        }

    def linear_gradient(
        start_hex: str, finish_hex: str = "#FFFFFF", n: int = 10
    ) -> ListedColormap:
        """
        Create a linear gradient palette.

        Returns a gradient list of (n) colors between
        two hex colors. start_hex and finish_hex
        should be the full six-digit color string,
        inlcuding the number sign ("#FFFFFF")

        Parameters
        ----------
        start_hex : str
            hex code for starting colour.
        finish_hex : str, optional
            hex code for finishing colour.
        n : int, optional
            number of colours in spectrum.

        No Longer Returned
        ------------------
        ListedColormap
            a gradient list of (n) colors between two hex colors.
        """
        # Starting and ending colors in RGB form
        s = hex_to_RGB(start_hex)
        f = hex_to_RGB(finish_hex)
        # Initilize a list of the output colors with the starting color
        RGB_list = [s]
        # Calcuate a color at each evenly spaced value of t from 1 to n
        for t in range(1, n):
            # Interpolate RGB vector for color at the current value of t
            curr_vector = [
                int(s[j] + (float(t) / (n - 1)) * (f[j] - s[j])) for j in range(3)
            ]
            # Add it to our list of output colors
            RGB_list.append(curr_vector)

        return color_dict(RGB_list)

    if diverging:
        newcmp = ListedColormap(
            linear_gradient(start_hex=low, finish_hex=medium_, n=n_ / 2)["hex"]
            + linear_gradient(start_hex=medium_, finish_hex=high, n=n_ / 2)["hex"]
        )
    else:
        newcmp = ListedColormap(
            linear_gradient(start_hex=low, finish_hex=high, n=n_)["hex"]
        )

    return newcmp


def calc_centroid(points: ndarray) -> ndarray:
    """
    Calculate the centroid from a numpy 2 dimenional array.

    Parameters
    ----------
    points : ndarray
        two dimensional ndarray of points/coordinates.

    Returns
    -------
    ndarray
        the centroid x an y coordinate as a ndarray e.g. `array([2., 3.])`.
    """
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    centroid = (sum(x) / len(points), sum(y) / len(points))
    return np.array(centroid)


def closest_node(query: ndarray, nodes: ndarray) -> int:
    """
    Find the closest node to the query position.

    Parameters
    ----------
    query : ndarray
        x and y coordinate of query e.g. `array([2., 3.])`
    nodes : ndarray
        x and y coordinates of all nodes.

    Returns
    -------
    int
        index position of closest node in all nodes list.
    """
    nodes = np.asarray(nodes[:, :2])
    deltas = nodes - query
    dist_2 = np.einsum("ij,ij->i", deltas, deltas)
    return np.argmin(dist_2)
