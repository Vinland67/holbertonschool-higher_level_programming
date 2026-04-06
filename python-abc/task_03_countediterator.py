#!/usr/bin/python3
"""
CountedIterator modulu - elementləri sayan iterator klası.
"""


class CountedIterator:
    """İteratoru genişləndirən və neçə element oxunduğunu sayan klas."""

    def __init__(self, iterable):
        """İteratoru və sayğacı başladır."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """İndiyə qədər neçə elementin oxunduğunu qaytarır."""
        return self.count

    def __next__(self):
        """Növbəti elementi qaytarır və sayğacı artırır."""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Obyektin özünü iterator kimi qaytarır."""
        return self
