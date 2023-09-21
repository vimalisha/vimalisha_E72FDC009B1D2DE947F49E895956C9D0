def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, producr in enumerate(productList):
     if product == targetProduct:
      indices.append(index)

  return indices

#example usage:
products = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(products, target)
print(result)