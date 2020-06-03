def sorter(item):
    return item['name']

presenters = [
    {'name': 'Susan', 'age':50},
    {'name': 'Christopher', 'age':47}
]

# presenters.sort() errors out
print(presenters)

presenters.sort(key=sorter)
print(presenters)

#using lambda 
presenters.sort(key=lambda item: len(item['name']))
print(presenters)
