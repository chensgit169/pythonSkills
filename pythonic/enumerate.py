from itertools import product


def generate_tuples_itertools(s):
    """ Generate tuples (n, m) where n, m are non-negative integers and n + m <= s."""
    return product(range(s + 1), repeat=2)


def generate_sub_sum(s):
    """
    Demonstrate change of summation order.
    Generate tuples (n+m, m-n) where n, m are integers ranging from 0 to s.
    """
    for sub in range(-s, s + 1):
        a = abs(sub)
        for k in range(a, s + 1):
            yield sub, 2 * k - a


def test_sub_sum():
    s = 3
    nm_list = list(generate_tuples_itertools(s))
    for sub, sum_ in generate_sub_sum(s):
        m = (sum_ + sub) // 2
        n = m - sub
        assert (n, m) in nm_list, f"({n}, {m}) not in nm_list"
        nm_list.remove((n, m))
    assert len(nm_list) == 0


test_sub_sum()

import numpy as np


def fourier_series_square(cn):
    """
    Given a list of Fourier coefficients with N components, return the square of as Fourier series.
    Namely, given

    c(t) = \sum_{n=0}^{N} c_n \exp(-int)

    compute

    A(t) = |c(t)|^2 = c(t) * c(t)^* = \sum_{n=-N}^{N} A_m^* \exp(-imt)

    """
    n = len(cn) - 1

    def mth_order(m):
        m_abs = abs(m)
        idx = np.arange(m_abs, n + 1)
        array_1 = cn[idx + (m + m_abs) // 2]
        array_2 = cn[idx - (m + m_abs) // 2].conj()
        A_m = array_1 @ array_2
        return A_m

    an = np.array([mth_order(m) for m in range(-n, n + 1)])
    return an
