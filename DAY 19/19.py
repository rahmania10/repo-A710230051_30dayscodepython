def calculate_area(shape):
  """
  Calculates the area of a shape based on its type.

  Args:
      shape: A dictionary with a "type" key and a "value" key specific to the shape type.

  Returns:
      The calculated area of the shape, or None if the shape type is not supported.
  """
  if shape["type"] == "square":
    return shape["value"] * shape["value"]
  elif shape["type"] == "circle":
    return 3.14159 * shape["value"] * shape["value"]
  else:
    print(f"Unsupported shape type: {shape['type']}")
    return None

# Example usage
square_area = calculate_area({"type": "square", "value": 5})
circle_area = calculate_area({"type": "circle", "value": 3})
triangle_area = calculate_area({"type": "triangle", "value": 4})  # Unsupported shape

print(f"Square area: {square_area}")  # Output: Square area: 25
print(f"Circle area: {circle_area:.2f}")  # Output: Circle area: 28.27
print(f"Triangle area: {triangle_area}")  # Output: Unsupported shape type: triangle
