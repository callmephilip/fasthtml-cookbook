from fasthtml.common import *

# UI

def prettify(f):
    def _f(*args, **kw): return f(*args, **(kw | { "cls": "block " + kw.get("cls","") }))
    return _f

@prettify
def Panel(*content, **kw): return Div(*content, **kw)

@prettify
def Textbox(*content, **kw): return Input(*content, **kw)

@prettify
def Password(*content, **kw): return Input(type="password", *content, **kw)

@prettify
def MultilineTextbox(*content, **kw): return Textarea(*content, **kw)

@prettify
def ActionButton(*content, **kw): return Button(*content, **kw)

def AddressBar(*content, **kw): return Textbox(*content, readonly=True, **kw)

on_response_error = """
  document.querySelector("#errors").innerHTML = event.detail.xhr.responseText;
  document.querySelector(".error-box").classList.add("show");
"""

def Playground(*content, path:str):
    return (
        ErrorBox(),
        Panel(AddressBar(value=f"🌎 http://localhost:8000{path}", cls="w-100"),
        Hr(), 
        *content,
        HtmxOn("responseError", on_response_error),
        cls="h-fullish")
    )

def ErrorBox():
    return Panel(
        Div(
            Div(P("Oh 🦌!")),
            Div(ActionButton("x", cls="display-inline", onclick="document.querySelector('.error-box').classList.remove('show')"), cls="flex-grow-1 text-align-right"),
            cls="flex flex-row"
        ),
        Hr(),
        P(id="errors"),
        cls="error-box"
    )

__all__ = ["Panel", "Textbox", "Password", "MultilineTextbox", "ActionButton", "Playground", "ErrorBox"]