class Bounds:
    def __init__(
        self,
        xmin=sys.float_info.max,
        ymin=sys.float_info.max,
        xmax=-sys.float_info.max,
        ymax=-sys.float_info.max,
    ):
        """Construct new bounds using given coordinates or default values."""
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
