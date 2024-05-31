def create_inventory(items):
    inventory= dict()
    for i in items:
        count= items.count(i)
        inventory[i]= count
    return inventory
print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))


def add_items(inventory, items):
    for i in set(items):
        count=items.count(i)
        if i in inventory:
            inventory[i]+= count
        else:
            inventory[i]=count
    return inventory
print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))


def decrement_items(inventory, items):
    for i in items:
        if i in inventory and inventory[i]>0:
            inventory[i] -=1
        elif inventory[i]<0:
            inventory[i]=0
    return inventory
print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"]))


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory
print(remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))

def list_inventory(inventory):
    lista=[]
    for k,v in inventory.items():
        if v > 0:
            a= (k,v)
            lista.append(a)
    return lista
print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))
