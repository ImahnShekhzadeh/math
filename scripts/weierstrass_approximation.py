"""
This script demonstrates the approximation of any continuous function defined
on the compact set `[a, b]` via Bernstein operators.
"""

import math
import os
from math import pi
from typing import Callable, List

import numpy as np
from matplotlib import pyplot as plt
from typeguard import typechecked


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

    assert j <= n, "Bernstein polynomial `\beta_{j}^{(n)}(x)` only defined for j <= n"
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
    function: Callable,
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
    function: Callable,
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
    function: Callable,
    argument: List[float] | np.ndarray,
    a: float = 0.0,
    b: float = 1.0,
) -> None:
    """
    Plot function and some elements of the Korovkin sequence approximating the
    continuous function.

    Args:
        korovkin_sequence: Each index contains a numpy array (evaluations for
            different x). First index corresponds to `n = 1`.
        -- cf. func `bernstein_operator()` for rest
    """

    n_max = len(korovkin_sequence)

    plt.plot(
        argument,
        function(argument),
        color="black",
        label="f",
    )
    plt.plot(argument, korovkin_sequence[1], label="B_2f", ls="--")
    plt.plot(argument, korovkin_sequence[10], label="B_{11}f", ls="--")
    plt.plot(argument, korovkin_sequence[-1], label=f"B_{{{n_max}}}f", ls="--")
    plt.legend(framealpha=0)
    plt.xlim(a - 0.01, b + 0.01)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.savefig(
        os.path.join(os.getcwd(), "approximation.pdf"),
        bbox_inches="tight",
        pad_inches=0.01,
        dpi=600,
    )
    plt.close()


@typechecked
def main() -> None:
    n = 500  # number of seq. elements to consider
    a, b = 0, pi  # function is approximated on `[a, b]`
    argument = np.linspace(start=a, stop=b, num=100, endpoint=True)  # x-values
    korovkin_sequence = bernstein_operator_sequence(
        n_max=n,
        function=function,
        argument=argument,
        a=a,
        b=b,
    )  # approximating polynomials


if __name__ == "__main__":
    main()
