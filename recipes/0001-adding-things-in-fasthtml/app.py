from fasthtml.common import *

app, rt = fast_app()

# 🚨 Do NOT use in-memory database in production!
db = database(":memory:")

# FastHTML will map this to a SQLite table
# How would you extend this schema? Maybe add
# creation/completion dates or both?
# could be handy for ordering tasks
# let's leave this as an exercise
class Todo: id: int; title: str; done: bool = False

# This will create table to host your Todos
# if it does not exist yet
todos = db.create(Todo, pk="id")
# Let's add some data so it does not feel lonely
todos.insert(Todo(title="call mom", done=True))
todos.insert(Todo(title="learn FastHTML"))

@patch
def __ft__(self: Todo):
  # implement __ft__ on your data class
  # to define how it's rendered
  # otherwise, you records will render 
  # as serialized strings
  return Li(
    Div(cls="line-thru" if self.done else "")(
        CheckboxX(checked=self.done),
        self.title
    )
  )

@rt("/add")
def post(title: str):
  #  notice how title got picked up from the form input
  return todos.insert(Todo(title=title))


@rt("/")
def get():
  # this is the landing page, it includes
  # a title
  # a list of existing Todos
  # and a form
  
  ts = Ul(id="ts")( # ⬅️ this ID is important!
    # notice how we pull all the tasks in the system
    # by simply calling `todos()`
    # thanks to MiniDataAPI 
    # https://docs.fastht.ml/explains/minidataapi.html
    # check ⬆️ for more details
    *[Li(todo) for todo in todos()]
  )

  nt = Form(
    # this form will POST to /add
    # whatever /add returns will be added 
    # as a last child
    # of the HTML element with `ts` as ID
    # which happens to be our task list from above ⬆️
    hx_post="/add", hx_target="#ts",
    # you a can also try hx_swap="afterbegin"
    # if you want new tasks to appear in the beginning
    hx_swap="beforeend")(
      Input(type="text",name="title",placeholder="Todo"),
      Button("Add")
  )

  # see how you can simply return this stuff as a tuple
  return H1("Things to do"), ts, nt

serve()
