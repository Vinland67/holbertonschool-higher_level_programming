#!/usr/bin/python3
"""
Fish, Bird və FlyingFish klaslarını ehtiva edən modul.
Çoxlu vərəsəlik (Multiple Inheritance) nümunəsi.
"""


class Fish:
    """Balıq klası."""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Quş klası."""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Uçan balıq klası - həm Fish, həm də Bird-dən miras alır."""
    
    def fly(self):
        """Bird-dən gələn fly metodunu override edir."""
        print("The flying fish is soaring!")

    def swim(self):
        """Fish-dən gələn swim metodunu override edir."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Hər iki valideyndən gələn habitat metodunu override edir."""
        print("The flying fish lives both in water and the sky!")
