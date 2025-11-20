from ObjectModels.exampleWebsite.exampleWebsiteObjects import *
from ObjectModels.exampleWebsite.learnMoreObjects import *
from Helpers.PlaywrightHelpers import *
from playwright.async_api import async_playwright, expect
import pytest

@pytest.mark.asyncio
async def test_loadExampleWebsite():
    async with async_playwright() as openPlaywright:
        # To show visuals uncomment this line
        # browserInstance = await openPlaywright.chromium.launch(channel="chrome", headless=False)
        browserInstance = await openPlaywright.chromium.launch(channel="chrome")
        examplePage = await browserInstance.new_page()
        assert await examplePage.title() != examplePageTitle, f"The webpage should be blank though has the title of {await examplePage.title()}. Please confirm what webpage is loaded."
        await examplePage.goto(exampleUrl)
        await waitForElementToBeVisible(examplePage, locateByRole(examplePage, exampleDefaultObjects["heading"]))

        assert await examplePage.title() == examplePageTitle, f"The webpage title should be {examplePageTitle} though has the title of {await examplePage.title()}. Confirm if the webpage title changed and update string in the exampleWebsiteObjects file."
        
        await verifyPageTitleAndClose(examplePage, examplePageTitle, browserInstance)

@pytest.mark.asyncio
async def test_clickLearnMoreFromExampleWebsite():
    async with async_playwright() as openPlaywright:
        # To show visuals uncomment this line
        # browserInstance = await openPlaywright.chromium.launch(channel="chrome", headless=False)
        browserInstance = await openPlaywright.chromium.launch(channel="chrome")
        examplePage = await browserInstance.new_page()
        assert await examplePage.title() != examplePageTitle, f"The webpage should be blank though has the title of {await examplePage.title()}. Please confirm what webpage is loaded."
        await examplePage.goto(exampleUrl)
        await waitForElementToBeVisible(examplePage, locateByRole(examplePage, exampleDefaultObjects["heading"]))
        
        # Going to Save Learn More Link to reduce searching for locator again.
        learnMoreLink = None

        for currentElementType, currentElementTraits in exampleDefaultObjects.items():
            currentElement = await checkDefaultElements(examplePage, currentElementTraits, returnElement=True)
            # Grab Learn More Link
            if currentElementType == "learnMore":
                learnMoreLink = currentElement

        # Negative Checks on main item on Learn More before changing screens
        assert examplePage.url != learnMoreUrl, f"The webpage URL should be {exampleUrl} instead has a URL of {await examplePage.url()}. Please confirm what website is appearing."
        assert await examplePage.title() != learnMorePageTitle, f"The webpage should be {examplePageTitle} though has the title of {await examplePage.title()}. Please confirm what webpage is loaded."

        await clickAndWaitForNewPageToBeVisible(examplePage, learnMoreLink, locateByRole(examplePage, learnMoreExampleDomainsObject))

        
        assert examplePage.url == learnMoreUrl, f"The webpage URL should be {learnMoreUrl} instead has a URL of {await examplePage.url()}. Please confirm what website is appearing."
        assert await examplePage.title() == learnMorePageTitle, f"The webpage title should be {learnMorePageTitle} though has the title of {await examplePage.title()}. Confirm if the webpage title changed and update string in the exampleWebsiteObjects file."
        
        await verifyPageTitleAndClose(examplePage, learnMorePageTitle, browserInstance)

@pytest.mark.asyncio
async def test_openLearnMoreAndClickAboutUsPage():
    async with async_playwright() as openPlaywright:
        # To show visuals uncomment this line
        # browserInstance = await openPlaywright.chromium.launch(channel="chrome", headless=False)
        browserInstance = await openPlaywright.chromium.launch(channel="chrome")
        examplePage = await browserInstance.new_page()
        assert await examplePage.title() != examplePageTitle, f"The webpage should be blank though has the title of {await examplePage.title()}. Please confirm what webpage is loaded."
        await examplePage.goto(exampleUrl)
        await waitForElementToBeVisible(examplePage, locateByRole(examplePage, exampleDefaultObjects["heading"]))
        
        # Going to Save Learn More Link to reduce searching for locator again.
        learnMoreLink = None

        for currentElementType, currentElementTraits in exampleDefaultObjects.items():
            currentElement = await checkDefaultElements(examplePage, currentElementTraits, returnElement=True)
            # Grab Learn More Link
            if currentElementType == "learnMore":
                learnMoreLink = currentElement

        await clickAndWaitForNewPageToBeVisible(examplePage, learnMoreLink, locateByRole(examplePage, learnMoreExampleDomainsObject))

        # Switching Page Instance since the webpage is off Example.com for cleaner variable checks
        learnMorePage = examplePage

        learnMoreHeaderMainObject = await checkDefaultElements(learnMorePage, learnMoreHeaderObject, returnElement=True)

        for currentElementTraits in learnMoreHeaderObjects.values():
            await checkChildElements(learnMorePage, learnMoreHeaderMainObject, currentElementTraits)

        for currentElementTraits in learnMoreLogoObjects.values():
            await checkChildElements(learnMorePage, learnMoreHeaderMainObject, currentElementTraits)

        # Going to Save About Element to reduce searching for locator again.
        aboutLink = None
        
        # Navigation Bar Elements Check and grab About Element
        for currentElementType, currentElementTraits in learnMoreNavigationObjects.items():
            currentElement = await checkChildElements(learnMorePage, learnMoreHeaderMainObject, currentElementTraits, returnElement=True, exactMatch=True)
            # Grab About Locator Element
            if currentElementType == "about":
                aboutLink = currentElement

        await clickAndWaitForNewPageToBeVisible(learnMorePage, aboutLink, locateByRole(learnMorePage, learnMoreExampleOurPolicyRemitObject))
        
        # Confirm Paragraph Count and text of page appears
        for currentAboutUsPageItem, currentAboutUsPageElement in learnMoreAboutUsPageObjects.items():
            elementLocator = locateByRole(learnMorePage, currentAboutUsPageElement)
            assert await elementLocator.is_visible(), f"Unable to find: {currentAboutUsPageItem} on the page: {learnMorePage}. Please confirm if the text has changed."
        await verifyPageTitleAndClose(learnMorePage, learnMorePageTitle, browserInstance)