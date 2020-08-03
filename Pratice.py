class Book():
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"You have a book title of {self.title} that was authored by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print(f"The book {self.title} has been deleted from your collection")


paulo_coelho = Book("The Alchemist", "Paulo Coelho", 208)
print(paulo_coelho)
print(len(paulo_coelho))
del paulo_coelho