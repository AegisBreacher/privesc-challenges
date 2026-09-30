def main():
    print("Hello!")
    print("Pick a number!")
    num = input("Enter: ")
    print("Awesome, I love " + str(num) +" too!")

def vuln():
    eval("__import__('os').system('cat /root/root.txt')")

if __name__ == "__main__":
    main()