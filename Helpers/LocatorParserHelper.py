import re
from playwright.async_api import Page, Locator

htmlElementTypeConverter = {
    "class" : ".",
    "universal" : "*",
    "id" : "#"
}

cssSelectorElementTypes = {
    "href",
    "src"
}

getByRoleElementConvertor = {
    "a": "link",
    "button": "button",
    "h1": "heading",
    "h2": "heading",
    "h3": "heading",
    "h4": "heading",
    "h5": "heading",
    "h6": "heading",
    "img": "img",
    "input": "textbox",
    "input[type='button']": "button",
    "input[type='submit']": "button",
    "input[type='checkbox']": "checkbox",
    "input[type='radio']": "radio",
    "input[type='search']": "searchbox",
    "input[type='email']": "textbox",
    "input[type='password']": "textbox",
    "input[type='number']": "spinbutton",
    "input[type='range']": "slider",
    "input[type='file']": "button",
    "label": "label",
    "li": "listitem",
    "ul": "list",
    "ol": "list",
    "menu": "menu",
    "nav": "navigation",
    "table": "table",
    "td": "cell",
    "th": "columnheader",
    "tr": "row",
    "tbody": "rowgroup",
    "thead": "rowgroup",
    "tfoot": "rowgroup",
    "select": "combobox",
    "option": "option",
    "textarea": "textbox",
    "form": "form",
    "article": "article",
    "section": "region",
    "aside": "complementary",
    "main": "main",
    "footer": "contentinfo",
    "header": "banner",
    "dialog": "dialog",
    "p": None,
    "i": None
}

def convertElementTypeToLocator(elementType, classText):
    if elementType == "class":
        return convertClassToSelector(classText)
    return htmlElementTypeConverter[elementType]

def grabLocator(currentPage, elementToFind, isParent=False, parentElement=None, exactMatch=False):
    if parentElement:
        currentPage = parentElement
    if isinstance(elementToFind, Locator):
        elementLocated = elementToFind
    elif "has_text" in elementToFind:
        elementLocated = currentPage.locator(elementToFind["htmlType"], has_text=elementToFind["has_text"])
    else:
        elementLocated = currentPage.locator(createLocatorElementString(elementToFind, exactMatch=exactMatch))
    return elementLocated

def convertClassToSelector(stringToConvert):
    """
    Convert Classes to valid .locator() string searches.
    This is to help create faster classes from object models without converting by hand
    
    Example:
        "hidden items-center gap-2 lg:flex" 
        
        converts to:

        ".hidden.items-center.gap-2.lg\\:flex"
    """

    if not stringToConvert:
        return ""
    grabAllClasses = stringToConvert.strip().split()
    def characterRemove(currentClass):
        currentClass = re.sub(r'([:\\[\]\/\(\)\#\+\~\=\.\,\'"])', r'\\\1', currentClass)
        return currentClass
    newClassSplit = [characterRemove(currentClass) for currentClass in grabAllClasses]
    combinedClassString = "." + ".".join(newClassSplit)
    return combinedClassString

def createLocatorElementString(elementToFind, exactMatch=False):
    htmlType, elementType, attributeText = elementToFind["htmlType"], elementToFind["locatorType"], elementToFind["locatorText"]
    if elementType in cssSelectorElementTypes:
        return f'{htmlType}[{elementType}="{attributeText}"]' if not exactMatch else f'{htmlType}[{elementType}="{attributeText}"]:text("{elementToFind["textCheck"]}")'
    locatorCharacter = convertElementTypeToLocator(elementType, attributeText)
    if elementType == "class":
        return htmlType+locatorCharacter
    else:
        return htmlType+locatorCharacter+attributeText

def locateByRole(currentPage, elementToFind, exactMatch=True, firstMatch=True):
    htmlType, elementText = getByRoleElementConvertor[elementToFind["htmlType"]], elementToFind["textCheck"]
    if htmlType == None:
        return currentPage.locator(elementToFind["htmlType"], has_text=elementText)
    if firstMatch:
        return currentPage.get_by_role(htmlType, name=elementText, exact=exactMatch).first
    else:
        return currentPage.get_by_role(htmlType, name=elementText, exact=exactMatch)

# Keeping for future reference
# CSS_SELECTORS = {
#     # --- Basic Selectors ---
#     "universal": {
#         "syntax": "*",
#         "description": "Selects all elements on the page",
#         "example": 'page.locator("*")',
#     },
#     "type": {
#         "syntax": "button",
#         "description": "Selects all <button> elements",
#         "example": 'page.locator("button")',
#     },
#     "id": {
#         "syntax": "#myId",
#         "description": "Selects element with id='myId'",
#         "example": 'page.locator("#myId")',
#     },
#     "class": {
#         "syntax": ".myClass",
#         "description": "Selects all elements with class='myClass'",
#         "example": 'page.locator(".myClass")',
#     },
#     "attribute_exact": {
#         "syntax": '[data-test="submit"]',
#         "description": "Selects elements with a specific attribute value",
#         "example": 'page.locator("[data-test=\\"submit\\"]")',
#     },

#     # --- Attribute Substring Matching ---
#     "attribute_contains": {
#         "syntax": '[title*="button"]',
#         "description": "Attribute contains the given substring",
#         "example": 'page.locator("[title*=\\"button\\"]")',
#     },
#     "attribute_starts_with": {
#         "syntax": '[id^="user_"]',
#         "description": "Attribute starts with the given substring",
#         "example": 'page.locator("[id^=\\"user_\\"]")',
#     },
#     "attribute_ends_with": {
#         "syntax": '[src$=".png"]',
#         "description": "Attribute ends with the given substring",
#         "example": 'page.locator("[src$=\\".png\\"]")',
#     },

#     # --- Grouping & Combinators ---
#     "grouping": {
#         "syntax": "h1, h2, h3",
#         "description": "Selects multiple element types",
#         "example": 'page.locator("h1, h2, h3")',
#     },
#     "descendant": {
#         "syntax": "div p",
#         "description": "Selects all <p> elements inside a <div>",
#         "example": 'page.locator("div p")',
#     },
#     "child": {
#         "syntax": "div > p",
#         "description": "Selects direct children only",
#         "example": 'page.locator("div > p")',
#     },
#     "adjacent_sibling": {
#         "syntax": "h1 + p",
#         "description": "Selects the first <p> immediately after an <h1>",
#         "example": 'page.locator("h1 + p")',
#     },
#     "general_sibling": {
#         "syntax": "h1 ~ p",
#         "description": "Selects all <p> siblings following an <h1>",
#         "example": 'page.locator("h1 ~ p")',
#     },

#     # --- Pseudo-classes ---
#     "first_child": {
#         "syntax": ":first-child",
#         "description": "Selects an element that is the first child of its parent",
#         "example": 'page.locator("ul li:first-child")',
#     },
#     "last_child": {
#         "syntax": ":last-child",
#         "description": "Selects the last child of a parent",
#         "example": 'page.locator("ul li:last-child")',
#     },
#     "nth_child": {
#         "syntax": ":nth-child(2)",
#         "description": "Selects the second child of a parent",
#         "example": 'page.locator("ul li:nth-child(2)")',
#     },
#     "not_selector": {
#         "syntax": ":not(.disabled)",
#         "description": "Selects elements that do NOT match the given selector",
#         "example": 'page.locator("button:not(.disabled)")',
#     },
#     "hover": {
#         "syntax": ":hover",
#         "description": "Selects element while hovered (pseudo-state)",
#         "example": 'page.locator("button:hover")',
#     },
#     "focus": {
#         "syntax": ":focus",
#         "description": "Selects element while focused",
#         "example": 'page.locator("input:focus")',
#     },
#     "checked": {
#         "syntax": ":checked",
#         "description": "Selects checked checkboxes or radio buttons",
#         "example": 'page.locator("input:checked")',
#     },

#     # --- Pseudo-elements ---
#     "before": {
#         "syntax": "::before",
#         "description": "Selects the ::before pseudo-element (not interactable in Playwright)",
#         "example": 'page.locator("button::before")',
#     },
#     "after": {
#         "syntax": "::after",
#         "description": "Selects the ::after pseudo-element (not interactable in Playwright)",
#         "example": 'page.locator("button::after")',
#     },

#     # --- Structural & State Selectors ---
#     "empty": {
#         "syntax": ":empty",
#         "description": "Selects elements with no children or text",
#         "example": 'page.locator("div:empty")',
#     },
#     "enabled": {
#         "syntax": ":enabled",
#         "description": "Selects enabled input/button elements",
#         "example": 'page.locator("button:enabled")',
#     },
#     "disabled": {
#         "syntax": ":disabled",
#         "description": "Selects disabled elements",
#         "example": 'page.locator("button:disabled")',
#     },

#     # --- Advanced Functional Selectors ---
#     "has": {
#         "syntax": ":has(img)",
#         "description": "Selects elements containing specific children",
#         "example": 'page.locator("div:has(img)")',
#     },
#     "has_text": {
#         "syntax": 'text="Submit"',
#         "description": "Selects element containing visible text (Playwright special)",
#         "example": 'page.locator("button", has_text="Submit")',
#     },
#     "nth_of_type": {
#         "syntax": ":nth-of-type(2)",
#         "description": "Selects the 2nd element of its type among siblings",
#         "example": 'page.locator("p:nth-of-type(2)")',
#     },
# }