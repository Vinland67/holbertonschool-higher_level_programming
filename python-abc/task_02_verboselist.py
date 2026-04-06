#!/usr/bin/python3
"""
Python siyahısını (list) genişləndirən və bildirişlər verən modul.
"""


class VerboseList(list):
    """Siyahı əməliyyatları zamanı mesaj çap edən klas."""

    def append(self, item):
        """Element əlavə edir və bildiriş verir."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        """Siyahını genişləndirir və neçə element əlavə olunduğunu bildirir."""
        count = len(x)
        super().extend(x)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Elementi silməzdən əvvəl bildiriş verir."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Elementi çıxarmazdan əvvəl bildiriş verir."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
