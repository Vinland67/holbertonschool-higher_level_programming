#!/usr/bin/python3
"""
Obyektin klasını və ya miras aldığı klasları yoxlayan modul.
"""


def is_kind_of_class(obj, a_class):
    """
    Obyektin müəyyən klasın instansı olub-olmadığını, yaxud 
    həmin klasdan miras alan klasdan olub-olmadığını yoxlayır.

    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Müqayisə ediləcək klas.

    Returns:
        bool: Uyğundursa True, yoxsa False.
    """
    return isinstance(obj, a_class)
