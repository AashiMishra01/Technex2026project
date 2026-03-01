from classifier import classify_image
import json

print("Starting test...")
result = classify_image("test3.jpeg")
print("Result received:")
print(json.dumps(result, indent=2))
print("Done!")

from carbon_engine import calculate_carbon_saved

# Example: manually set weight (or None to use default)
user_weight = None   # change to 0.5 for manual test

carbon_result = calculate_carbon_saved(
    result["object_detected"],
    result["waste_category"],
    user_weight
)

print("\nCarbon Impact:")
print(carbon_result)
