from jinja2 import Template

janapith_data = [{"year":1965, "awardees": "G Sankara Kurup", "language":"Malayalam"},
                 {"year":1933, "awardees": "A Shri Kurup", "language":"Hindi"},
                 {"year":2002, "awardees": "Kasrhish Muttal", "language":"Marathi"},
                 {"year":1999, "awardees": "Khishi Jain", "language":"Punjabi"}]

def main():
    # Read the template file content into a variable
    template_file = open('app2.html.jinja2')
    TEMPLATE = template_file.read()
    template_file.close()

    # Render the template using Jinja2
    template = Template(TEMPLATE)
    content = template.render(janapith_data=janapith_data)

    # Save the rendered html document
    my_html_doc = open("janapith.html","w")
    my_html_doc.write(content)
    my_html_doc.close()

if __name__ == "__main__":
    # execute only if run as a script
    main()