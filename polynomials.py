from numpy import polyadd, polysub, polymul, polydiv

poly1 = [3, 2, -1]  # define 3x² + 2x - 1
poly2 = [4, -1, 3]  # define 4x² - x + 3

result = polyadd(poly1, poly2)
print(result)

result2 = polysub(poly1, poly2)  # (3x² + 2x - 1) - (4x² - x + 3)
print(result2)

result3 = polymul(poly1, poly2)  # (3x² + 2x - 1) * (4x² - x + 3)
print(result3)

result4 = polydiv(poly1, poly2)  # (3x² + 2x - 1) / (4x² - x + 3)
print(result4)