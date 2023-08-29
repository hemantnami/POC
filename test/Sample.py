
import requests
from lxml import html

# URL of the website you want to scrape
url = 'https://demo.automationtesting.in/Register.html'

# Fetch the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content
tree = html.fromstring(html_content)

# Initialize an empty list to store generated XPath expressions
xpath_expressions = []

def generate_xpath(element):
    # Generate an XPath expression for the provided element
    xpath = tree.getpath(element)
    return xpath

# Interactive loop to generate XPath expressions
while True:
    print("Select an element by entering its index:")
    for index, element in enumerate(tree.iter(), start=1):
        print(f"{index}: {element.tag}")
    
    try:
        selected_index = int(input("Enter the index (0 to exit): "))
        if selected_index == 0:
            break
        selected_element = list(tree.iter())[selected_index - 1]
        xpath = generate_xpath(selected_element)
        xpath_expressions.append(xpath)
        print(f"Generated XPath: {xpath}\n")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid index.\n")

# Print the generated XPath expressions
print("Generated XPath expressions:")
for index, xpath in enumerate(xpath_expressions, start=1):
    print(f"{index}: {xpath}")
