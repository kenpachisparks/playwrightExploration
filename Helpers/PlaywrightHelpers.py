from Helpers.LocatorParserHelper import *
from ObjectModels.HomePageObjects import *

from playwright.async_api import async_playwright, Page, expect, Locator

async def verifyPageTitleAndClose(currentPage, currentPageTitle, browserInstance):
    await currentPage.title() == currentPageTitle, f"Expected title() to be '{currentPageTitle}', but received {await currentPage.title()}"
    currentPage.is_closed(), f"{currentPageTitle} is closed when it should still be opened."
    await browserInstance.close()
    currentPage.is_closed(), f"{currentPageTitle} didn't close out properly."

async def scrollToElementOnScreen(currentPage, elementToFind, returnElement=False):
    elementToScrollTo = grabLocator(currentPage, elementToFind)
    await elementToScrollTo.scroll_into_view_if_needed()
    return elementToScrollTo if returnElement else None

async def checkDefaultElements(currentPage, elementAttributes, negativeCheck=False, returnElement=False, howManyLocators=0):
    if isinstance(elementAttributes, Locator):
        elementToCheck = elementAttributes
    else:
        elementToCheck = grabLocator(currentPage, elementAttributes)
    
    
    if not negativeCheck and "textCheck" in elementAttributes:
        await checkElementText(currentPage, elementToCheck, elementAttributes['textCheck'])
    if "altText" in elementAttributes:
        await checkElementAltText(currentPage, elementToCheck, elementAttributes['altText'])
    if negativeCheck:
        assert await elementToCheck.count() == 0, f"Element with attributes {elementAttributes} was found on the page: {await currentPage.title()}, which shouldn't appear. Please confirm why this element exists."
    else:
        if howManyLocators > 1:
            assert await elementToCheck.count() == howManyLocators, f"Element with attributes {elementAttributes} was found on the page: {await currentPage.title()}, though should have {howManyLocators} locator's and instead found {await elementToCheck.count()}."
        else:
            assert await elementToCheck.is_visible(), f"Couldn't find the on the page:{await currentPage.title()}, with attributes {elementAttributes}. Please check if the element exists. Currtent Locator is: {elementToCheck}"
    if returnElement:
        return elementToCheck

async def checkElementText(currentPage, currentElement, expectedText, negativeCheck=False):
    if negativeCheck:
        assert await currentElement.text_content() != expectedText, f"The element {currentElement} should not have the default text of {expectedText}. The text_content() is: {await currentElement.text_content()}. Please confirm the visual text on the page: {await currentPage.title()}."
    else:
        assert await currentElement.text_content() == expectedText, f"The element {currentElement} does not have the default text of {expectedText}. The text_content() is: {await currentElement.text_content()}. Please confirm the visual text on the page: {await currentPage.title()}."

async def checkElementAltText(currentPage, currentElement, altText):
    await checkAttributeOfElement(currentPage, currentElement, "alt", altText)

async def checkAttributeOfElement(currentPage, currentElement, attribute, expectedAttributeVaule):
    assert await currentElement.get_attribute(attribute) == expectedAttributeVaule, f"The element {currentElement} does not have the '{attribute}' attribute of '{expectedAttributeVaule}'. The attribute is: {await currentElement.get_attribute(attribute)}. Please confirm the attribute element on the page: {await currentPage.title()}."

async def checkChildElements(currentPage, parentElement, childAttributes, negativeCheck=False, returnElement=False, nthIndex=0, exactMatch=False):
    elementToCheck = parentElement.locator(createLocatorElementString(childAttributes, exactMatch=exactMatch))
    elementToCheck = await countChecker(elementToCheck, nthIndex)
    assert await elementToCheck.is_visible(), f"Couldn't find the on the page:{await currentPage.title()}, with attributes {childAttributes}. Please check if the element exists."
    return elementToCheck

async def countChecker(elementToCheck, nthIndex):
    return elementToCheck.nth(nthIndex) if await elementToCheck.count() > 1 else elementToCheck

async def clickAndWaitForNewPageToBeVisible(currentPage, currentElement, newPageElementType):
    await currentElement.click()
    await waitForElementToBeVisible(currentPage, newPageElementType)

async def waitForElementToBeVisible(currentPage, elementToWaitFor):
    if isinstance(elementToWaitFor, Locator):
        elementToWaitFor = elementToWaitFor
    else:
        elementToWaitFor = grabLocator(currentPage, elementToWaitFor)
    await expect(elementToWaitFor).to_be_visible()