
# Accepting user input

def get_non_empty_text(prompt):
    value = input(prompt).strip()
    if not value:
        raise ValueError("Input cannot be empty.")
    return value


def get_positive_integer(prompt, min_value=0, max_value=120):
    value = input(prompt).strip()

    if not value.isdigit():
        raise ValueError("Input must be a valid integer.")

    number = int(value)

    if number < min_value or number > max_value:
        raise ValueError("Value out of acceptable range.")

    return number


def get_float_in_range(prompt, min_value, max_value):
    value = input(prompt).strip()

    try:
        number = float(value)
    except ValueError:
        raise ValueError("Input must be a numeric value.")

    if number < min_value or number > max_value:
        raise ValueError("Value out of acceptable range.")

    return number


def get_sample_id(prompt):
    value = input(prompt).strip().upper()

    if not value.startswith("LAB-"):
        raise ValueError("Sample ID must start with 'LAB-'.")

    numeric_part = value.replace("LAB-", "")
    if not numeric_part.isdigit():
        raise ValueError("Sample ID must contain digits after 'LAB-'.")

    return value


def main():
    print("=== Secure Lab Input System ===")

    try:
        patient_name = get_non_empty_text("Enter patient name: ")
        patient_age = get_positive_integer("Enter patient age: ", 0, 120)
        sample_id = get_sample_id("Enter sample ID (LAB-XXXX): ")
        hb = get_float_in_range("Enter Hemoglobin value (g/dL): ", 5.0, 25.0)

    except ValueError as error:
        print(f"Input error: {error}")
        return

    print("\n--- Input Summary ---")
    print(f"Patient Name: {patient_name}")
    print(f"Age: {patient_age}")
    print(f"Sample ID: {sample_id}")
    print(f"Hb: {hb} g/dL")

    print("\nData accepted. Proceed to analysis.")


if __name__ == "__main__":
    main()
