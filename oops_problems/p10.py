class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return f"{self.title} | {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self,other):
        return self.title == other.title
    
    def __repr__(self):
        return f"Book('{self.title}','{self.author}','{self.pages}')"
    
b1 = Book("Harry Potter", "J.K Rowling", 500)
b2 = Book("Harry Potter", "Someone Else", 300)
b3 = Book("Atomic Habits", "James Clear", 400)

print(b1)
print(len(b1))
print(b1 == b2)     
print(b1 == b3)     
print(repr(b1))     