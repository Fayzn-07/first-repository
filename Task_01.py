inventory = {
    "Laptop": 10,
    "Smartphone": 25,
    "Tablet": 15,
    "Headphones": 30,
    "Smartwatch": 20
}
inventory.update({"Smartphone":10})
inventory.update({"Headphones":5})
print("New items avialable in the stock",inventory)

inventory.get("Smartwatch")
print("'Smartwatch' is removed from the inventory in quantity:",inventory.pop("Smartwatch"))
print("Updated inventory!:",inventory)

if "Camera" in inventory:
    print("Camera is available in the inventory!")
else:
    print("Camera is not available in the inventory!")
