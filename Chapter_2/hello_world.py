
def main():
    print("Hello World!")
    a = testing()
    a / 0

def testing() -> int:
    return "abc"

if __name__ == "__main__":
    main()
