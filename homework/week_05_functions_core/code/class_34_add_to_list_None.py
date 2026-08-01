# add_to_list likho jo default None use kare, 3 alag baar call karke dikhao har baar fresh list aati hai.
# Write a function add_to_list(item, data=None) that uses None as the default value. Call it three different times to show that each call gets a fresh list.


#1
def add_to_list(item, data=None):

    if data is None:
        data = []
    data.append(item)
    return data

print(add_to_list("Apple"))
print(add_to_list("Banana"))
print(add_to_list("Orange"))

