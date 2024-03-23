def linear(progress):
    return progress


def flip(progress):
    return 1 - progress


def ease_in_quad(progress):
    return progress * progress


def ease_out_quad(progress):
    return flip(flip(progress) ** 2)


def ease_in_out_quad(progress):
    if progress < 0.5:
        return 2 * ease_in_quad(progress)
    return flip((-2 * progress + 2) ** 2 / 2)



