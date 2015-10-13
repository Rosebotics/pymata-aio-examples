"""
Uses the rosegraphics library that we use in the first half of 120.
"""

import rosegraphics as rg


def main():
    window = rg.RoseWindow(300, 200)

    circle = rg.Circle(rg.Point(100, 100), 50)
    circle.fill_color = 'red'
    circle.attach_to(window)

    window.render()
    window.close_on_mouse_click()

main()
