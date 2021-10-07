import os


names = ['TrungLV', 'Jeff', 'Gary', 'Jill', 'Samantha']

print("\n =================================")
for name in names:
    print("Hello there, " + name)
    print(" ".join(["Hello there,", name]))

print("\n =================================")
print(", ".join(names))

print("\n =================================")
location_of_files = "."
file_name = "example.txt"
print(location_of_files + '\\' + file_name)
with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())

print("\n =================================")
who = "TrungLV"
how_many = 12
#TrungLV bought 12 apples today!
# sentence
print(who, "bought", how_many, 'apples today!')
print("{} bought {} apples today!".format(who, how_many))

