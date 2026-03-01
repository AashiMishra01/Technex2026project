# EPA-based emission factors (kg CO2 saved per kg recycled)
emission_factors = {
    "plastic": 1.5,
    "paper": 0.9,
    "glass": 0.3,
    "metal": 9.1,
    "cardboard": 0.9,
    "food": 0.5
}

# Default fallback by category
category_factors = {
    "Recyclable": 1.5,
    "Biodegradable": 0.5,
    "Hazardous": 2.0  # treated as avoided contamination impact
}

# Default average weights (kg)
default_weights = {
    "plastic": 0.03,
    "metal": 0.5,
    "paper": 0.02,
    "glass": 0.4,
    "cardboard": 0.05,
    "battery": 0.05
}


def calculate_carbon_saved(object_detected, waste_category, weight_kg=None):

    object_detected = object_detected.lower()

    # If user did not provide weight, use default
    if weight_kg is None:
        weight_kg = default_weights.get(object_detected, 0.1)

    # Prefer material-specific factor
    factor = emission_factors.get(
        object_detected,
        category_factors.get(waste_category, 1.0)
    )

    co2_saved = weight_kg * factor
    trees_equivalent = co2_saved / 21  # 1 tree absorbs ~21 kg CO2/year

    return {
        "weight_used_kg": round(weight_kg, 3),
        "co2_saved_kg": round(co2_saved, 2),
        "trees_equivalent": round(trees_equivalent, 2)
    }