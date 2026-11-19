class Publication:
    def __init__(self, title: str, author: str):
        self._title = title
        self._author = author

    def get_title(self) -> str:
        return self._title

    def set_title(self, title: str):
        self._title = title

    def get_author(self) -> str:
        return self._author

    def set_author(self, author: str):
        self._author = author

    def display_info(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")


class Book(Publication):
    def __init__(self, title: str, author: str, number_of_pages: int):
        super().__init__(title, author)
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self) -> int:
        return self._number_of_pages

    def set_number_of_pages(self, number_of_pages: int):
        if number_of_pages <= 0:
            print("The number of pages must be positive")
            self._number_of_pages = 0
        else:
            self._number_of_pages = number_of_pages

    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self._number_of_pages}")


class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.set_issue_number(issue_number)

    def get_issue_number(self) -> int:
        return self._issue_number

    def set_issue_number(self, issue_number: int):
        if issue_number <= 0:
            print("The issue number must be positive")
            self._issue_number = 0
        else:
            self._issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue number: {self._issue_number}")



publication1 = Publication("The Impact of Social Media on Mental Health: A Review of Literature", "Smith, J., & Williams, L. (2020)")
book1 = Book("Don Quixote", "Miguel de Cervantes", 100)
magazine1 = Magazine("The New Yorker", "Malcom Gladwell, Jhumpa Lahiri, Stephen King", 200)

print("Publication Information:")
publication1.display_info()

print("\nBook Information:")
book1.display_info()

print("\nMagazine Information:")
magazine1.display_info()