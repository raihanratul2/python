mylist = ["10", 20, "30"]

print(repr(mylist))

class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"book(title='{self.title}', author='{self.author}')"

mybook=book("Himur Hate Nil Podmo", "Humayun Ahmed")
print(repr(mybook))

x = [1, '2', 3]
newx = eval(repr(x))
print(f"x= {x}\nnewx = {newx} \n and their types x = {type(x)} , newx = {type(newx)} , {type(repr(x))}")
if x == newx:
    print(f"True  x==newx")