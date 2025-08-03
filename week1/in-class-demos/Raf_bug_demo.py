# run this in Python Console
raf = (1, ["Jake"])
print(f"{raf=}")
# raf.append("Tiffany")  # error: tuple has no attribute append
raf[1].append("Tiffany")
print(f"{raf=}")  # output: [1, ['Jake', 'Tiffany']
raf[1] += ["Luke"]  # TypeError: 'tuple' object does not support item assignment
print(f"{raf=}")  # output: [1, ['Jake', 'Tiffany', 'Luke]
