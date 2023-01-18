def data_compression(data):
    compress_result = ""
    i = 0
    while i < len(data):
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
            i += 1

        compress_result += str(count) + data[i]
        i += 1

    return compress_result


data = "555888888811111111AAAAAAAHHHHHHIIIIIIII"
print("Compressed data: ", data_compression(data), end="\n")
user_input = input("Enter some data: ")
print("Compressed data: ", data_compression(user_input))
