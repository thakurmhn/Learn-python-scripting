def describe_book(name, author, **book_description):
    book_details={}
    book_details['book_name'] = name
    book_details['author'] = author

    for key, value in book_description.items():
        book_details[key] = value

    return book_details

book1=describe_book('My Experiment with Truth', 'MK Gandhi', publishedin='1943', publishedby='Mukharji Publications')
print(book1)

