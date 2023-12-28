import pyhtml as h

t = h.html(
    h.head(
        h.title("Test Page")
    ),
    h.body(
        h.h1("This is a title"),
        h.div("This is some text in a div"),
        h.div(h.h2("Inside title"),
        h.p("Some text in a paragraph"))
    )
)

print(t.render())