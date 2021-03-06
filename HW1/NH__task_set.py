# Write a Python program to check if two given sets have no elements in common.

x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}
print("Original set elements:")
print(x)
print(y)
print(z)

print("\nConfirm two given sets have no element(s) in common:")

print(f"For sets x and y: {x.isdisjoint(y)}")
print(f"For sets x and z: {x.isdisjoint(z)}")
print(f"For sets z and y: {z.isdisjoint(y)}")


# Write a Python program to remove the intersection of a 2nd set from the 1st set.

sn1 = {1, 2, 3, 4, 5}
sn2 = {4, 5, 6, 7, 8}
print("Original sets:")
print(sn1)
print(sn2)

sn1.difference_update(sn2)
print("Sets after removing the intersection from the 1st set")
print(sn1)
print(sn2)

