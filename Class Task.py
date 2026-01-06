books = {
    "The Great Gatsby": 15.99,
    "To Kill a Mockingbird": 12.49,
    "1984": 10.99,
    "Pride and Prejudice": 9.99,
    "Moby Dick": 8.99
}   

backup_Copy=books.copy()
books = {
    "The Great Gatsby": 15.99,
    "To Kill a Mockingbird": 12.49,
    "1984": 10.99,
    "Pride and Prejudice": 9.99,
    "Moby Dick": 8.99
}   


backup_Copy=books.copy()
print("\n===>Books in Inventory:")
print("----------------")
for book, price in books.items():
    print("Book Name:", book)
    print("=>Price: $:", price)
total_Revenue=sum(books.values())
print("Total Revenue:$",total_Revenue)
print("----------------")
if "1984" in books:
    print("1984 is sold out from the inventory at price of $:",books["1984"])
    books.pop("1984")
else:
    print("Book not found in the inventory!") 
print("----------------")   