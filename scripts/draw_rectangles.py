import os

import matplotlib.pyplot as plt
from typeguard import typechecked


@typechecked
def draw_rectangle(x_1: float, x_2: float, width: float, height: float) -> None:
    """
    Draw a rectangle, where the bottom left corner is specified by the
    coordinates `x_1` and `x_2`.
    """

    assert width > 0 and height > 0

    rect = plt.Rectangle(
        (x_1, x_2),
        width=1,
        height=1,
        linewidth=1,
        linestyle="--",
        edgecolor="black",
        facecolor="none",
    )
    ax = plt.gca()
    ax.add_patch(rect)


def main():
    u_1, u_2 = 1, 1
    v_1, v_2 = 1.5, 1.5
    width = 1
    height = 1

    plt.figure()
    draw_rectangle(x_1=u_1, x_2=u_2, width=width, height=height)
    draw_rectangle(x_1=v_1, x_2=v_2, width=width, height=height)
    plt.xlim(0, max(u_1, v_1) + width + 0.05)
    plt.ylim(0, max(u_2, v_2) + height + 0.05)
    plt.savefig(
        os.path.join(os.getcwd(), "rectangles.pdf"),
        bbox_inches="tight",
        pad_inches=0.01,
        dpi=600,
    )
    plt.close()


if __name__ == "__main__":
    main()
