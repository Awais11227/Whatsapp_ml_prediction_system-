def parse_features(message, expected_count):

    # Clean message completely
    cleaned = message.strip().replace(" ", "").rstrip(",")

    # Split safely
    parts = cleaned.split(",")

    # Convert to float safely
    try:
        values = [float(x) for x in parts if x != ""]
    except:
        raise ValueError("All values must be numeric")

    # Strict check
    if len(values) != expected_count:
        raise ValueError(
            f"Expected {expected_count} values, got {len(values)}"
        )

    return values