# Also on Youtube: https://youtube.com/shorts/V1q-ndAHkqM
from fasthtml.common import *

# Default app come with Pico.css
# hooked up automatically
# see https://picocss.com/
app, rt = fast_app()

@dataclass
class Book: title: str; author: str; img: str

@patch
def __ft__(self: Book):
    return Article(
        Section(
            Img(src=self.img, alt=f"{self.title} by {self.author}", style="max-height: 350px;"),
            Div(
                Button(
                    NotStr("""
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                            <path d="M8 2.748l-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z" ></path>
                        </svg>
                    """)
                ),
                Button(
                    NotStr("""
                        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-play-circle-fill" viewBox="0 0 16 16">
                            <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM6.79 5.093A.5.5 0 0 0 6 5.5v5a.5.5 0 0 0 .79.407l3.5-2.5a.5.5 0 0 0 0-.814l-3.5-2.5z" ></path>
                        </svg>
                    """)
                ),
                Button(
                    NotStr("""
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-three-dots" viewBox="0 0 16 16">
                            <path d="M3 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z" ></path>
                        </svg>
                    """)
                )
            )
        ),
        Section(
            H3(self.title),
            P(self.author)
        )
    )

books = [
    Book('Dune', 'Frank Herbert', 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1555447414i/44767458.jpg'),
    Book('Brave New World', 'Aldous Huxley', 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1575509280i/5129.jpg'),
    Book('Fahrenheit 451', 'Ray Bradbury', 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1383718290i/13079982.jpg')
]

@rt("/")
def get(): return Main(**{"onClick": "window.location.href = 'http://0.0.0.0:7778/'"})(Div(H1("Made for you"), Section(*[book for book in books])))

serve(port=7777)
