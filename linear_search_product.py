def linear_search_product(product_list, target_product):
    indices = []
    
    for i in range(len(product_list)):
        if product_list[i] == target_product:
            indices.append(i)
    
    return indices
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target_product = "Apple"
result = linear_search_product(products, target_product)
print(result)  # Output: [0, 3, 5]

target_product = "Mango"
result = linear_search_product(products, target_product)
print(result)  # Output: []
