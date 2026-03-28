#!/usr/bin/env python3
"""julia_set - Julia set ASCII renderer."""
import sys
CHARS = " .:-=+*#%@"
def julia(cx=-0.7, cy=0.27015, w=80, h=30, max_iter=80):
    for row in range(h):
        line = ""
        for col in range(w):
            x = -2.0 + 4.0 * col / w
            y = -1.5 + 3.0 * row / h
            i = 0
            while x*x + y*y <= 4 and i < max_iter:
                x, y = x*x - y*y + cx, 2*x*y + cy; i += 1
            line += CHARS[i * (len(CHARS)-1) // max_iter]
        print(line)
if __name__ == "__main__":
    cx = float(sys.argv[1]) if len(sys.argv) > 1 else -0.7
    cy = float(sys.argv[2]) if len(sys.argv) > 2 else 0.27015
    julia(cx, cy)
