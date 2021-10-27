# ITEM
### Item properties 
```python
class Item:
    def __init__(self,user_id,name,qty,price):
        self.user_id = user_id
        self.name = name
        self.qty = qty
        self.price = price
```
### Item create 
```cmd
item create <id> <name> <qty> <price>
```
### Item find by id
```cmd
item find <id>
```
### Item find all
```cmd
item find all
```
### Item search 
```cmd
item search <key> <value>
```
