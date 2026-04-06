#!/usr/bin/python3
"""
Mixin-lərdən istifadə edərək Dragon klasını yaradan modul.
"""


class SwimMixin:
    """Üzmə bacarığı verən Mixin."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Uçma bacarığı verən Mixin."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Həm üzə, həm də uça bilən Əjdaha klası."""
    def roar(self):
        """Əjdahaya məxsus nərilti metodu."""
        print("The dragon roars!")
