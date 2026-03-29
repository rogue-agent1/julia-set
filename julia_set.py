#!/usr/bin/env python3
"""Julia Set - Render Julia set fractals for various c parameters."""
import sys

def julia(z, c, max_iter=100):
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > 2: return i
    return max_iter

def render(c, x_min=-2, x_max=2, y_min=-1.5, y_max=1.5, width=70, height=25, max_iter=80):
    chars = " .'`^\",;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    lines = []
    for row in range(height):
        y = y_min + (y_max - y_min) * row / height
        line = ""
        for col in range(width):
            x = x_min + (x_max - x_min) * col / width
            n = julia(complex(x, y), c, max_iter)
            if n == max_iter: line += " "
            else: line += chars[n % len(chars)]
        lines.append(line)
    return "\n".join(lines)

PRESETS = {
    "classic": -0.7 + 0.27015j,
    "dendrite": 0j + 1j,
    "rabbit": -0.123 + 0.745j,
    "siegel": -0.391 - 0.587j,
    "spiral": -0.8 + 0.156j,
}

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "classic"
    c = PRESETS.get(name, PRESETS["classic"])
    print(f"=== Julia Set ({name}, c={c}) ===\n")
    print(render(c))

if __name__ == "__main__":
    main()
