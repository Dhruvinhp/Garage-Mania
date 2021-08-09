
try:
    # TODO dfsdfagv
    from .production import *
except ImportError:
    try:
        from .dev import *
    except ImportError as e:
        raise Exception("settings files are missing")
