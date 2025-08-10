import time
from datetime import datetime, timezone, timedelta


def unix_to_local_time(unix_timestamp, timezone_offset_seconds):
    """
    Converts a Unix timestamp to a human-readable local time string.

    Parameters:
    - unix_timestamp (int): The Unix timestamp (seconds since Jan 1, 1970 UTC).
    - timezone_offset_seconds (int): The timezone offset in seconds (e.g., +3600 for UTC+1).

    Returns:
    - str: Local time formatted as "HH:MM AM/PM".

    Example:
        unix_timestamp = 1754832000  # corresponds to 2025-08-10 12:00:00 UTC
        timezone_offset_seconds = 7200  # +2 hours offset

        local_time = unix_to_local_time(unix_timestamp, timezone_offset_seconds)
        print(local_time)  # Output: "02:00 PM"
    """

    local_time = datetime.utcfromtimestamp(unix_timestamp) + timedelta(seconds=timezone_offset_seconds)
    return local_time.strftime("%I:%M %p")