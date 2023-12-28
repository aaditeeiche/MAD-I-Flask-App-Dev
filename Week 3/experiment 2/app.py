from jinja2 import Template
temp = """Hello {{ name }}"""

TEMPLATE = """Hello, this is {p:+} and this is {n:x}"""
# the plus sign means it print the sign of the number too
# :d decimal format, :x hexadecimal format

def main():
    # print(TEMPLATE.format(name="Aaditee"))
    print(TEMPLATE.format(p=5, n=-237))
    t = Template(temp)
    print(t.render(name="Aadi"))

if __name__ == "__main__":
    # execute only if run as a script
    main()


# python -m venv .experiment2-env [command to create a virtual environment locally]
# pip freeze [shows all of the installed packages] then do this: pip freeze > requirements.txt