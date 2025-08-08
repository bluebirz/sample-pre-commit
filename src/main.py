def adder(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b


def main():
    a: int = 1
    b: int = 2
    print(f"{a} + {b} = {adder(1, 2)}")  # Example usage of the adder function


if __name__ == "__main__":
    main()
