import datetime

# Function to convert readable time to Unix timestamp
def to_unix_timestamp(date_string, time_string="00:00:00"):
    """Converts a given date and time string to a Unix timestamp."""
    dt = datetime.datetime.strptime(f"{date_string} {time_string}", "%Y-%m-%d %H:%M:%S")
    unix_timestamp = int(dt.timestamp())
    return unix_timestamp

# Example Usage
sdate_input = "2025-02-10"  # Example date
stime_input = "00:00:00"    # Example time (optional, defaults to midnight)

edate_input = "2025-02-11"
etime_input = "00:00:00"


start_utime = to_unix_timestamp(sdate_input, stime_input)
end_utime = to_unix_timestamp(edate_input, etime_input)
print(f"Unix Timestamp: {start_utime} {end_utime}")
