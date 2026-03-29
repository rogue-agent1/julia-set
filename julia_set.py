import argparse

def julia(z, c, max_iter):
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2: return i
    return max_iter

def main():
    p = argparse.ArgumentParser(description="Julia set renderer")
    p.add_argument("-w", "--width", type=int, default=80)
    p.add_argument("-H", "--height", type=int, default=30)
    p.add_argument("-i", "--iterations", type=int, default=50)
    p.add_argument("--cr", type=float, default=-0.7)
    p.add_argument("--ci", type=float, default=0.27015)
    args = p.parse_args()
    c = complex(args.cr, args.ci)
    chars = " .:-=+*#%@"
    for row in range(args.height):
        line = ""
        for col in range(args.width):
            x = -1.5 + 3.0 * col / args.width
            y = -1.0 + 2.0 * row / args.height
            m = julia(complex(x, y), c, args.iterations)
            line += chars[m % len(chars)] if m < args.iterations else " "
        print(line)

if __name__ == "__main__":
    main()
