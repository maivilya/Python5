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


def data_recovery(compressed_data):
    recovery_result = ""
    i = 0
    while i < len(compressed_data):
        while i + 1 < len(compressed_data) and compressed_data[i] == compressed_data[i + 1]:
            recovery_result += compressed_data[i]
            i += 1

        i += 1

    return recovery_result


# data = "555888888811111111AAAAAAAHHHHHHIIIIIIII"
# print("Compressed data: ", data_compression(data), end="\n")
user_input = input("Enter some data: ")
print("Compressed data: ", data_compression(user_input))
print("Recovery data: ", data_recovery(user_input))

# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
