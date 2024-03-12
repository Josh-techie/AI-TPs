# Read the file here

try:
    # with open("test.txt", "r") as f:
    with open("emojis.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line, end=" ")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)

finally:
    f.close()

# But Now let's imagine the file contains some emojis, if we try the code above with a
# file that contains emojis, we will get an error.
# Why? You may wonder 🤔
# Because the file is encoded in a different way, and the default encoding is not able to decode it

# Emojis are represented by Unicode characters, which may not be compatible with the
# default encoding used by the open() function in Python. Therefore, when the code tries
# to read the file, it may encounter an error or may not be able to display
# the emojis correctly.

# We will basically just need to specify the type of encoding while openeing the file

# We will simply transform the code above to this:
#     with open("test.txt", "r") as f:
#         to:
#     with open("test.txt", "utf-8") as f: