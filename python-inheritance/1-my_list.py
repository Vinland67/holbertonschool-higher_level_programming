#!/usr/bin/python3
"""
MyList klasını ehtiva edən modul.
"""


class MyList(list):
    """Siyahıdan miras alan klas."""

    def print_sorted(self):
        """Siyahını artan sıra ilə (ascending) çap edir."""
        print(sorted(self))
