from datetime import datetime, timedelta


def unix_to_local_time(unix_timestamp, timezone_offset_seconds):
    """
    Converts a Unix timestamp to a human-readable local time string.

    Parameters:
    - unix_timestamp (int): The Unix timestamp (seconds since Jan 1, 1970 UTC).
    - timezone_offset_seconds (int): The timezone offset in seconds (e.g., +3600 for UTC+1).

    Returns:
    - str: Local time formatted as "HH:MM AM/PM".

    """

    local_time = datetime.utcfromtimestamp(unix_timestamp) + timedelta(seconds=timezone_offset_seconds)
    return local_time.strftime("%I:%M %p")