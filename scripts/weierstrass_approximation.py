"""
This script demonstrates how to approximate the function sin(x) on [0, pi]
via Bernstein operators.
"""

from math import pi
import math
from typing import List, Callable

import numpy as np
from typeguard import typechecked
from matplotlib import pyplot as plt


@typechecked
def function(
    argument: float | List[float] | np.ndarray[float],
) -> float | np.ndarray[float]:
    """
    Take the function that we want to approximate and evaluate it.

    Args:
        argument: x-values at which to evaluate the function

    Returns:
        f(x)
    """
    if type(argument) == float:
        return math.sin(argument)
    else:
        return np.sin(argument)


@typechecked
def bernstein_polynomial(
    argument: List[float] | np.ndarray[float],
    j: int,
    n: int,
    a: float = 0.0,
    b: float = 1.0,
) -> np.ndarray:
    """
    Evaluate the Bernstein polynomial `\beta_{j}^{(n)}(x)` on `[a, b]` for a
    fixed `j` and `n`.

    Args:
        argument: x-values
        j: index
        n: degree of Bernstein polynomials
        a: lower bound of compact set `[a, b]`
        b: upper bound of compact set `[a, b]`

    Returns:
        Bernstein polynomials `\beta_j^{(n)}(x)`
    """
    if type(argument) == list:
        argument = np.array(argument)

    assert (
        j <= n
    ), "Bernstein polynomial `\beta_{j}^{(n)}(x)` only defined for j <= n"
    assert n >= 0, "Bernstein polynomials are only defined for natural `n`"
    assert (np.min(argument) >= a) and (
        np.max(argument) <= b
    ), f"Please ensure that the x-values lie in `[{a}, {b}]`. Did you forget to provide `a` and `b`?"

    # do affine mapping of `[a, b]` to `[0, 1]` via `(x - a) / (b - a)`
    return (
        math.comb(n, j)
        * np.power((argument - a) / (b - a), j)
        * np.power(1 - (argument - a) / (b - a), n - j)
    )


@typechecked
def bernstein_operator(
    n: int,
    function: Callable[float, float],
    argument: List[float] | np.ndarray,
    a: float = 0.0,
    b: float = 1.0,
) -> np.ndarray:
    """
    Evaluate the Bernstein operators `B_n: C[a, b] -> P_n`, where `C[a, b]`
    denotes the space of continuous functions on `[a, b]` and `P_n` the space
    of algebraic polynomials of degree at most `n`.

    Args:
        n: degree of Bernstein polynomials
        function: continuous function on `[a, b]`
        argument: x-values
        a: lower bound of compact set `[a, b]`
        b: upper bound of compact set `[a, b]`

    Returns:
        Bernstein operators applied to `f`, i.e. `(B_nf)(x)`
    """
    bernstein_operator_eval = np.zeros_like(argument)
    for j in range(0, n + 1):
        np.add(
            bernstein_operator_eval,
            function((b - a) * j / n + a)  # affine mapping `[0, 1] -> [a, b]`
            * bernstein_polynomial(argument, j, n, a, b),
            bernstein_operator_eval,
            casting="unsafe",
        )

    return bernstein_operator_eval


@typechecked
def bernstein_operator_sequence(
    n_max: int,
    function: Callable[float, float],
    argument: List[float] | np.ndarray,
    a: float = 0.0,
    b: float = 1.0,
) -> List[np.ndarray]:
    """
    Look at elements of the sequence `(B_nf)`.

    Argument:
        n_max: Look at sequence elements `B_1f, B_2f, ..., B_{n_max}f`.
        -- cf. func `bernstein_operator()` for rest

    Returns:
        List, where each list index corresponds to an array, which contains
        the bernstein operator evaluations for different arguments
    """
    assert n_max >= 1, "B_nf can only be considered for n >= 1"

    sequence = []
    for n in range(1, n_max + 1):
        sequence.append(bernstein_operator(n, function, argument, a, b))

    return sequence


@typechecked
def plot(
    korovkin_sequence: List[np.ndarray],
    function: Callable[float, float],
    argument: List[float] | np.ndarray,
    a: float = 0.0,
    b: float = 1.0,
) -> None:
    plt.plot()


@typechecked
def main() -> None:
    a, b = 0, pi / 2
    korovkin_sequence = bernstein_operator_sequence(
        n_max=100,
        function=function,
        argument=np.linspace(start=a, stop=b, num=100, endpoint=True),
        a=a,
        b=b,
    )
    print(f"Korovkin sequence:\n\n{korovkin_sequence}")


if __name__ == "__main__":
    main()
