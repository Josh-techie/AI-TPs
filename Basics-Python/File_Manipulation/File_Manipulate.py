# Read the file here

try:
    with open("test.txt", "r") as f:
        for line in f:
            print(line, end=" ")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)

finally:
    f.close()
    

