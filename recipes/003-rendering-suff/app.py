from fasthtml.common import *

app, rt = fast_app()

# return a string
# @rt('/')
# def index(): 
#     # return a string from route handler
#     # sends plain text back to the client, no markup, no html
#     # this also means no <head> or <body> tags  
#     return "Hello"

# return a FastTag component
# FastHTML has over 150 FT components designed to accelerate web development. 
# Most of these mirror HTML tags such as <div>, <p>, <a>, <title>, and more. However, there are some extra tags added, including:
# @rt('/')
# def index():
#     # FT stands for "FastTags"
#     # FT components turn Python objects into HTML.
#     # A domain-specific language (DSL) is a computer language specialized to a particular application domain.  
#     # returning an FT component, renders it to HTML, also includes <head> and <body> tags 
#     return H1("Hello world")

# getting comfortable with FastTags: attributes
# @rt('/')
# def index():
#     # this outputs
#     # <label hx-get="/get-date" for="element_id" x-init="console.log('👋 alpinejs')" class="btn">FastHTML</label>
#     return Label(
#         cls="btn", # <- class attribute becomes cls to prevent conflict with Python reserved keyword
#         hx_get="/get-date", # <- htmx specific attributes are remapped to Python friendly versions with underscores
#         _for="element_id", # <- _for renders to for
#         **{ "x-init": "console.log('👋 alpinejs')" }  # <- any additional attributes with more adventurous names can passed via a dictionary
#     )("FastHTML")

# and, of course you can build component hierarchies by nesting FastTags
# @rt('/')
# def index():
#     # this outputs
#     # <div>
#     #   <h1>Hello world</h1>
#     #   <a 
#     #       href="https://fastht.ml" 
#     #       hx-get="/get-date"
#     #       x-init="console.log('👋 alpinejs')"
#     #       class="btn"><img src="https://fastht.ml/assets/logo.svg" alt="FastHTML Logo"
#     #   >FastHTML</a>
#     #  </div>
#     return Div(
#         H1("Hello world"),
#         A(
#             href="https://fastht.ml",
#             cls="btn", # <- class attribute becomes cls to prevent conflict with Python reserved keyword
#             hx_get="/get-date", # <- htmx specific attributes are remapped to Python friendly versions with underscores
#             **{ "x-init": "console.log('👋 alpinejs')" }  # <- any additional attributes with more adventurous names can passed via a dictionary
#         )(
#             Img(src="https://fastht.ml/assets/logo.svg", alt="FastHTML Logo"),
#             "FastHTML"
#         )
#     )


# NotStr fasttag
# @rt('/')
# def index():
#     # this outputs
#     # <div>
#     #    <p>&lt;div&gt;This won&#x27;t work&lt;/div&gt;</p>
#     #    <div>This will work</div>
#     # </div>
#     # normally if your fast tags include strings with markup inside
#     # they will be escaped, but not when used in conjunction with NotStr
#     return Div(
#         P("<div>This won't work</div>"),
#         NotStr("<div>This will work</div>")
#     )


# from fasthtml.components import FastHTML_CookBook

# # automagically create your own HTML tags
# @rt('/')
# def index():
#     # this outputs:
#     # <fasthtml-cookbook></fasthtml-cookbook>
#     return FastHTML_CookBook()


# composing FastTags to create your own components
# @rt('/')
# def index():
#     # this outputs:
#     # <div>
#     #    <h1>Hello world</h1>
#     #    <a href="https://fastht.ml">FastHTML</a>
#     # </div>
#     def MyComponent():
#         return Div(
#             H1("Hello world"),
#             A(href="https://fastht.ml")("FastHTML")
#         )
#     return MyComponent()

# turning ordinary Python objects into FastTags
# @rt('/')
# def index():
#     # this outputs: <a href="https://fastht.ml">FastHTML</a>
#     @dataclass
#     class Website: name: str; url: str

#     @patch
#     def __ft__(self: Website): return A(href=self.url)(self.name)

#     return Website("FastHTML", "https://fastht.ml")


# # you can return a list of fast tags like this
# @rt('/')
# def index():
#     # this outputs:
#     # <div>Hello</div>
#     # <div>World</div>
#     return [Div("Hello"), Div("World")]

# or using tuple
# @rt('/')
# def index():
#     # this outputs:
#     # <div>Hello</div>
#     # <div>World</div>
#     return Div("Hello"), Div("World")

# however, when composing fasttags, make sure to spread the list
@rt('/')
def index():
    # this outputs:
    # <div>
    #   <div>Hello</div>
    #   <div>World</div>
    # </div>
    return RedirectResponse("/login")


serve()
