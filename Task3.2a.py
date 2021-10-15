pwd = "jasdJW+l/*/b"

specials = 0

for char in pwd:
    if "+" in char or "-" in char or "*" in char or "/" in char:
        specials += 1

print(specials)
