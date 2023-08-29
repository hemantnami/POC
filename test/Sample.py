
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
def retrieve_locators(element):
    # Retrieve locators for the given element
    xpath = driver.execute_script(
        "function absoluteXPath(element) {"
        "   var comp, comps = [];"
        "   var parent = null;"
        "   var xpath = '';"
        "   var getPos = function(element) {"
        "       var position = 1, curNode;"
        "       if (element.nodeType == Node.ATTRIBUTE_NODE) {"
        "           return null;"
        "       }"
        "       for (curNode = element.previousSibling; curNode; curNode = curNode.previousSibling) {"
        "           if (curNode.nodeName == element.nodeName) {"
        "               ++position;"
        "           }"
        "       }"
        "       return position;"
        "   };"
        "   while (element !== null && element.nodeType === Node.ELEMENT_NODE) {"
        "       comp = comps[comps.length] = {};"
        "       comp.name = element.nodeName.toLowerCase();"
        "       comp.position = getPos(element);"
        "       comp.prefix = null;"
        "       comp.localName = null;"
        "       xpath = '/' + comp.name + '[' + comp.position + ']' + xpath;"
        "       element = element.parentNode;"
        "   }"
        "   return xpath;"
        "};"
        "return absoluteXPath(arguments[0]);", element
    )
    css_selector = element.value_of_css_property('selector')

    return xpath, css_selector

# Iterate through all elements on the page and retrieve locators
elements = driver.find_elements_by_xpath("//*")
for element in elements:
    xpath, css_selector = retrieve_locators(element)
    print(f"XPath: {xpath}")
    print(f"CSS Selector: {css_selector}")
    print("=" * 30)

# Close the browser
driver.quit()

