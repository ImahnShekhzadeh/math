import os

import matplotlib.pyplot as plt
from typeguard import typechecked


@typechecked
def draw_circle(x_1: float, x_2: float, radius: float) -> None:
    """
    Draw a circle with center given by `x_1` and `x_2` and a specified radius.

    Args:
        x_1: x-coordinate of center
        x_2: y-coordinate of center
        radius: radius of circle
    """

    assert radius > 0

    rect = plt.Circle(
        (x_1, x_2),
        radius=radius,
        linewidth=1,
        linestyle="--",
        edgecolor="olive",
        facecolor="none",
    )
    plt.axis("equal")  # https://stackoverflow.com/a/9232513
    ax = plt.gca()
    ax.add_patch(rect)


def main():
    u_1, u_2 = 1, 1
    v_1, v_2 = 4, 4
    x = (2.1, 3.0)  # point in intersection
    r_1 = 3
    r_2 = 4

    plt.figure()
    draw_circle(x_1=u_1, x_2=u_2, radius=r_1)
    draw_circle(x_1=v_1, x_2=v_2, radius=r_2)
    plt.plot(u_1, u_2, "o", color="black", markersize=2)
    plt.plot(v_1, v_2, "o", color="black", markersize=2)
    plt.plot(x[0], x[1], "o", color="black", markersize=2)
    plt.text(u_1 - 0.1, u_2 - 0.5, r"$\tilde{x}$", size=12)
    plt.text(v_1 - 0.1, v_2 - 0.4, r"$x'$", size=12)
    plt.text(x[0] - 0.1, x[1] - 0.4, r"$x$", size=12)
    plt.plot([u_1, x[0]], [u_2, x[1]], linewidth=1, color="tab:cyan")  # line
    plt.plot([v_1, x[0]], [v_2, x[1]], linewidth=1, color="tab:cyan")  # line
    plt.xlim(
        min(u_1, v_1) - max(r_1, r_2) - 0.2,
        max(u_1, v_1) + max(r_1, r_2) + 0.2,
    )
    plt.ylim(
        min(u_2, v_2) - max(r_1, r_2) - 0.2,
        max(u_2, v_2) + max(r_1, r_2) + 0.2,
    )
    plt.xticks([], [])
    plt.yticks([], [])
    plt.savefig(
        os.path.join(os.getcwd(), "circles.pdf"),
        bbox_inches="tight",
        pad_inches=0,
        dpi=600,
    )
    plt.close()


if __name__ == "__main__":
    main()
