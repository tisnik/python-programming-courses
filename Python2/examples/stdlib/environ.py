import os


def get_event_level():
    """Get level of events to monitor (errors only, or error and warnings)."""
    if os.environ.get("SENTRY_CATCH_WARNINGS", False):
        return logging.WARNING
    return logging.ERROR
