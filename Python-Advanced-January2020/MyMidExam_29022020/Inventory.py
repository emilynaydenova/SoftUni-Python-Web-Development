# Inventory

inventory = input().split(', ')

while (command := input()) != 'Craft!':
    action, item = command.split(' - ')
    if action == 'Collect':
        if item not in inventory:
            inventory.append(item)
    elif action == 'Drop':
        if item in inventory:
            inventory.remove(item)
    elif action == 'Combine Items':
        oldItem, newItem = item.split(':')
        if oldItem in inventory:
            idx = inventory.index(oldItem)
            inventory.insert(idx+1,newItem)
    elif action == 'Renew':
        if item in inventory:
            idx = inventory.index(item)
            inventory.pop(idx)
            inventory.append(item)
print(', '.join(inventory))
