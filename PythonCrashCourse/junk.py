class Dog():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def sit(self):
        print(f"{self.name} is now sitting")
    def rollover(self):
        print(f"{self.name} is now rolling over")

class Book():
    def __init__(self, name, author):
        self.book_name=name
        self.author_name=author

    def describe_book(self, **book_description):
        book_details={}
        book_details['book_name'] = name
        book_details['author'] = author

        for key, value in book_description.items():
            book_details[key] = value

        return book_details

#book1=Book('my experiment with truth', 'M K Gandhi')
#print(book1.describe_book(published_in=1942, published_by='mukharji publications'))


class chocolate():
    def __init__(self, name):
        self.name=name

    def describe_chocolate(self, **more_about):
        chocolate_details={}
        chocolate_details['chocolate_name'] = 'name'

        for key, value in more_about.items():
            chocolate_details[key] = value

        return chocolate_details

favorite_chocolate=chocolate('Kismi')

print(f"My Favorite Chocolate is {favorite_chocolate.name}")


