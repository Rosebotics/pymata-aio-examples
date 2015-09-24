a = (249).to_bytes(1, byteorder='big')
print(str(a))

b = int.from_bytes(a, byteorder='big')
print(str(b))
