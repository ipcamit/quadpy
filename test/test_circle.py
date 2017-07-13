# -*- coding: utf-8 -*-
#
from helpers import \
        create_monomial_exponents2, \
        integrate_monomial_over_unit_circle, \
        check_degree

from matplotlib import pyplot as plt
import pytest
import quadpy


@pytest.mark.parametrize(
    'scheme',
    [quadpy.circle.Equidistant(k) for k in range(1, 6)]
    )
def test_scheme(scheme):
    degree = check_degree(
            lambda poly: quadpy.circle.integrate(
                poly, [0.0, 0.0], 1.0, scheme
                ),
            integrate_monomial_over_unit_circle,
            create_monomial_exponents2,
            scheme.degree + 1
            )
    assert degree == scheme.degree
    return


@pytest.mark.parametrize(
    'scheme',
    [quadpy.circle.Equidistant(3)]
    )
def test_show(scheme):
    quadpy.circle.show(scheme)
    return


if __name__ == '__main__':
    scheme_ = quadpy.circle.Equidistant(30)
    test_scheme(scheme_)
    test_show(scheme_)
    plt.show()
