# Copyright (c) ShaHm

import os

from config import autoclean


async def auto_clean(popped):
    if not popped:
        return
    try:
        rem = popped["file"]
        if rem in autoclean:
            autoclean.remove(rem)
        count = autoclean.count(rem)
        # URLs and queue markers are never files.  isfile also prevents an
        # accidental attempt to remove arbitrary/nonexistent paths.
        if count == 0 and isinstance(rem, str) and os.path.isfile(rem):
            try:
                os.remove(rem)
            except OSError:
                pass
    except:
        pass
