import random

def list_of_hexa_colors(num_colors):
    """Generates a list of hexadecimal color codes."""
    hex_digits = "0123456789abcdef"
    colors = []
    for _ in range(num_colors):
        color = "#"
        for _ in range(6):
            color += random.choice(hex_digits)
        colors.append(color)
    return colors

def list_of_rgb_colors(num_colors):
    """Generates a list of RGB color codes."""
    colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f"rgb({r}, {g}, {b})")
    return colors

def generate_colors(color_type, num_colors):
    """Generates a list of hexadecimal or RGB color codes."""
    if color_type == "hexa":
        return list_of_hexa_colors(num_colors)
    elif color_type == "rgb":
        return list_of_rgb_colors(num_colors)
    else:
        return "Invalid color type."

print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))