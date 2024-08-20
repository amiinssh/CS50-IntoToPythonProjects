def convert(time_str):
    def parse_time(time_str):
        """Parse a time string into hours, minutes, and period (AM/PM)."""
        if "AM" in time_str:
            time_str = time_str.replace("AM", "").strip()
            period = "AM"
        elif "PM" in time_str:
            time_str = time_str.replace("PM", "").strip()
            period = "PM"
        else:
            raise ValueError("Invalid time format.")

        if ":" in time_str:
            hours, minutes = time_str.split(":")
        else:
            hours, minutes = time_str, "00"

        return int(hours), int(minutes), period

    def to_24_hour_format(hours, minutes, period):
        """Convert 12-hour time to 24-hour format."""
        if period == "AM":
            if hours == 12:
                hours = 0
        elif period == "PM":
            if hours != 12:
                hours += 12

        if not (0 <= hours < 24 and 0 <= minutes < 60):
            raise ValueError("Invalid time value.")

        return f"{hours:02}:{minutes:02}"

    # Split the input string into start and end times
    try:
        start_time_str, end_time_str = time_str.split(" to ")
    except ValueError:
        raise ValueError("Invalid format. Expected 'start_time to end_time'.")

    # Parse both times
    start_hours, start_minutes, start_period = parse_time(start_time_str)
    end_hours, end_minutes, end_period = parse_time(end_time_str)

    # Convert both times to 24-hour format
    start_time_24 = to_24_hour_format(start_hours, start_minutes, start_period)
    end_time_24 = to_24_hour_format(end_hours, end_minutes, end_period)

    return f"{start_time_24} to {end_time_24}"


# Example usage
if __name__ == "__main__":
    test_cases = [
        "9:00 AM to 5:00 PM",
        "9 AM to 5 PM",
        "9:00 AM to 5 PM",
        "9 AM to 5:00 PM",
        "12:00 AM to 12:00 PM",
        "12:00 PM to 12:00 AM",
        "1:00 AM to 1:00 PM",
        "1 AM to 1 PM",
    ]

    for test in test_cases:
        try:
            print(f"{test} -> {convert(test)}")
        except ValueError as e:
            print(f"Error with input '{test}': {e}")
