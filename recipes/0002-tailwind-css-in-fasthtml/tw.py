# Also on Youtube: https://youtube.com/shorts/V1q-ndAHkqM
# design credit: https://www.creative-tim.com/twcomponents/component/music-player-cards

from fasthtml.common import *


# Do NOT do this in production
# check https://tailwindcss.com/docs/installation
# for more info on how to get updated tailwindcss
# bundles ready for when you are ready to go to prod 
tw = Script(src="https://cdn.tailwindcss.com")
app, rt = fast_app(pico=False, hdrs=[tw, Script(src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"), Script(code="""
    window.addEventListener("load", () => { confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } }); })
""")])

@dataclass
class Book: title: str; author: str; img: str

@patch
def __ft__(self: Book):
    return Article(cls='bg-gray-900 shadow-lg rounded p-3')(
        Section(cls='group relative')(
            Img(src=self.img, alt=f"{self.title} by {self.author}", cls='w-full md:w-72 block rounded'),
            Div(cls='absolute bg-black rounded bg-opacity-0 group-hover:bg-opacity-60 w-full h-full top-0 flex items-center group-hover:opacity-100 transition justify-evenly')(
                Button(cls='hover:scale-110 text-white opacity-0 transform translate-y-3 group-hover:translate-y-0 group-hover:opacity-100 transition')(
                    NotStr("""
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                            <path d="M8 2.748l-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z" ></path>
                        </svg>
                    """)
                ),
                Button(cls='hover:scale-110 text-white opacity-0 transform translate-y-3 group-hover:translate-y-0 group-hover:opacity-100 transition')(
                    NotStr("""
                        <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-play-circle-fill" viewBox="0 0 16 16">
                            <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM6.79 5.093A.5.5 0 0 0 6 5.5v5a.5.5 0 0 0 .79.407l3.5-2.5a.5.5 0 0 0 0-.814l-3.5-2.5z" ></path>
                        </svg>
                    """)
                ),
                Button(cls='hover:scale-110 text-white opacity-0 transform translate-y-3 group-hover:translate-y-0 group-hover:opacity-100 transition')(
                    NotStr("""
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-three-dots" viewBox="0 0 16 16">
                            <path d="M3 9.5a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z" ></path>
                        </svg>
                    """)
                )
            )
        ),
        Section(cls='p-5')(
            H3(self.title, cls='text-white text-lg'),
            P(self.author, cls='text-gray-400')
        )
    )

books = [
    Book('Dune', 'Frank Herbert', 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1555447414i/44767458.jpg'),
    Book('Brave New World', 'Aldous Huxley', 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1575509280i/5129.jpg'),
    Book('Fahrenheit 451', 'Ray Bradbury', 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1383718290i/13079982.jpg')
]

@rt("/")
def get():
    return Main(cls='grid place-items-center min-h-screen bg-[#f2f3fa] p-5')(
        Div(
            H1("Made for you", cls='text-4xl sm:text-5xl md:text-7xl font-bold mb-5'),
            Section(cls='grid grid-cols-1 sm:grid-cols-3 gap-4')(
                *[book for book in books]
            )
        )
    )

serve(port=7778, app="app")
