#
# 8. Taking apart filenames
#
# my solution
# def extract_place(filename):
#     first = filename.find("_")
#     return filename[first + 1:filename.find("_", first + 1)]

# alternative solution
# def extract_place(filename):
#     first = filename.find("_")
#     partial = filename[first + 1:]
#     second = partial.find("_")
#     return partial[:second]

# another alternative solution using the split method


def extract_place(filename):
    return filename.split("_")[1]


print(extract_place("2018-06-06_MountainView_16:20:00.jpg"))
