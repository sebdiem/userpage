import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path

def angle_in_minus_half_pi_three_half_pi(angle):
    """Returns the value of `angle` in $[-\frac{\pi}{2}; 3\frac{\pi}{2}]$."""
    while angle >= 3*np.pi/2:
        angle -= 2*np.pi
    while angle < -np.pi/2:
        angle += 2*np.pi
    return angle

def vector_to_angle(u):
    """Returns the angle between vector `u` and the `x` axis."""
    return np.arctan2(u[1], u[0])

def angle_to_vector(angle):
    """Returns the unit vector making an angle `angle` with the `x` axis."""
    return np.r_[np.cos(angle), np.sin(angle)]

def rotation(theta, two_dim=False):
    """Returns the rotation matrix of angle `theta`.
    Optional arguments:
        two_dim     : if `True` the shape of the returned matrix is `(2,2)`
                      else, the shape is `(3,3)` and the corresponding rotation
                      is around the `z` axis."""
    cos, sin = np.cos(theta), np.sin(theta)
    result = np.array([[cos, -sin, 0],
                       [sin,  cos, 0],
                       [  0,    0, 1]])
    return result[:2,:2] if two_dim else result

def get_polygon_patch(vertices, **kwargs):
    """Returns a `matplotlib.PathPatch` representing a polygon defined by its
    `vertices`."""
    codes = [Path.MOVETO] + (len(vertices) - 1)*[Path.LINETO] + [Path.CLOSEPOLY]
    path = Path(vertices + [(0., 0.)], codes)
    patch = PathPatch(path, **kwargs)
    return patch

def lines_intersection(P1, u1, P2, u2):
    u1 = u1/(u1.dot(u1))**0.5
    u2 = u2/(u2.dot(u2))**0.5
    u1_dot_u2 = u1.dot(u2)
    if u1_dot_u2**2 == 1.: return None
    l = (P2-P1).dot(u1 - u2*(u1_dot_u2))/(1. - u1_dot_u2**2)
    return P1 + l*u1

def rectangle_vertices(*corners_coords):
    left, bottom, right, top = corners_coords
    # left is the leftmost x coord, right the rightmost x coord ...
    return [np.r_[left, bottom], np.r_[right, bottom], np.r_[right, top], np.r_[left, top]]
