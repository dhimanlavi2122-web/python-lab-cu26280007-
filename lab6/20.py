set20_a = {1, 2}
set20_b = {"x", "y"}
cartesian_product = set()

for item_a in set20_a:
    for item_b in set20_b:
        cartesian_product.add((item_a, item_b))

print("20.", cartesian_product)

