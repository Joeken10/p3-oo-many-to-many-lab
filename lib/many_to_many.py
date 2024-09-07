class Author:
    _all = []

    def __init__(self, name):
        self.name = name
        Author._all.append(self)

    def contracts(self):
        
        return [contract for contract in Contract._all if contract.author == self]

    def books(self):
        
        return list(set([contract.book for contract in self.contracts()]))

    def sign_contract(self, book, date, royalties):
        
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    _all = []

    def __init__(self, title):
        self.title = title
        Book._all.append(self)

    def contracts(self):
        # Returns all contracts where the book is the current instance
        return [contract for contract in Contract._all if contract.book == self]

    def authors(self):
        # Returns a list of authors who have contracts for the book
        return list(set([contract.author for contract in self.contracts()]))


from datetime import datetime

class Contract:
    _all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract._all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
       
        return [contract for contract in cls._all if contract.date == date]



def test_contract_contracts_by_date():
    """Test Contract class has method contracts_by_date() that filters contracts by date"""
    Contract._all = [] 
    author1 = Author("Name 1")
    book1 = Book("Title 1")
    book2 = Book("Title 2")
    book3 = Book("Title 3")
    author2 = Author("Name 2")
    book4 = Book("Title 4")
    contract1 = Contract(author1, book1, "02/01/2001", 10)
    contract2 = Contract(author1, book2, "01/01/2001", 20)
    contract3 = Contract(author1, book3, "03/01/2001", 30)
    contract4 = Contract(author2, book4, "01/01/2001", 40)

  
    contracts_on_date = Contract.contracts_by_date("01/01/2001")

    
    expected_contracts = [contract2, contract4]
    
    assert contracts_on_date == expected_contracts



