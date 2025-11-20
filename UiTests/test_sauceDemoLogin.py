from ObjectModels.sauceWebsite.sauceWebsiteObjects import *
from Helpers.PlaywrightHelpers import *
from playwright.async_api import async_playwright

import pytest


@pytest.mark.asyncio
async def test_printTitle():
    async with async_playwright() as openPlaywright:
        # To show visuals uncomment this line
        # browserInstance = await openPlaywright.chromium.launch(channel="chrome", headless=False)
        browserInstance = await openPlaywright.chromium.launch(channel="chrome")
        sauceWebpage = await browserInstance.new_page()

        assert await sauceWebpage.title() != sauceWebpage, f"The webpage should be blank though has the title of {await sauceWebpage.title()}. Please confirm what webpage is loaded."
        await sauceWebpage.goto(sauceUrl)
        await waitForElementToBeVisible(sauceWebpage, saucePageBeforeLoginObjects["heading"])
        assert await sauceWebpage.title() == saucePageTitle, f"The webpage title should be {saucePageTitle} though has the title of {await saucePageTitle.title()}. Confirm if the webpage title changed and update string in the exampleWebsiteObjects file."
        
        # Print Page Title
        print(f"\n\nWebpage Title is: {await sauceWebpage.title()}\n\n")
        
        await verifyPageTitleAndClose(sauceWebpage, saucePageTitle, browserInstance)

@pytest.mark.asyncio
async def test_sauceLogInFlow():
    async with async_playwright() as openPlaywright:
        # To show visuals uncomment this line
        # browserInstance = await openPlaywright.chromium.launch(channel="chrome", headless=False)
        browserInstance = await openPlaywright.chromium.launch(channel="chrome")
        sauceWebpage = await browserInstance.new_page()

        assert await sauceWebpage.title() != sauceWebpage, f"The webpage should be blank though has the title of {await sauceWebpage.title()}. Please confirm what webpage is loaded."
        await sauceWebpage.goto(sauceUrl)
        await waitForElementToBeVisible(sauceWebpage, saucePageBeforeLoginObjects["heading"])

        for currentElementType, currentElementTraits in saucePageErrorLoginObjects.items():
            await checkDefaultElements(sauceWebpage, currentElementTraits, negativeCheck=True)

        # Going to Save Learn More Link to reduce searching for locator again.
        logInElements = {}

        for currentElementType, currentElementTraits in saucePageBeforeLoginObjects.items():
            logInElements[currentElementType] = await checkDefaultElements(sauceWebpage, currentElementTraits, returnElement=True)
        
        await logInElements["userNameField"].fill(sauceUserName)
        await logInElements["passwordField"].fill(saucePassword)
        assert await logInElements["userNameField"].input_value() == sauceUserName, f'Username Text Field does not have the username {sauceUserName}, instead has the value of {await logInElements["userNameField"].input_value()}.'
        assert await logInElements["passwordField"].input_value() == saucePassword, f'Password Text Field does not have the username {saucePassword}, instead has the value of {await logInElements["passwordField"].input_value()}.'

        await clickAndWaitForNewPageToBeVisible(sauceWebpage, logInElements["logInButton"], grabLocator(sauceWebpage, successfulLogInObject))
        
        await verifyPageTitleAndClose(sauceWebpage, saucePageTitle, browserInstance)

@pytest.mark.asyncio
async def test_confirmErrorLoginAlertsAppear(caplog):
    async with async_playwright() as openPlaywright:
        # To show visuals uncomment this line
        # browserInstance = await openPlaywright.chromium.launch(channel="chrome", headless=False)
        browserInstance = await openPlaywright.chromium.launch(channel="chrome")
        sauceWebpage = await browserInstance.new_page()
        await sauceWebpage.goto(sauceUrl)
        await waitForElementToBeVisible(sauceWebpage, saucePageBeforeLoginObjects["heading"])

        # Going to Save Learn More Link to reduce searching for locator again.
        logInElements = {}

        for currentElementType, currentElementTraits in saucePageBeforeLoginObjects.items():
            logInElements[currentElementType] = await checkDefaultElements(sauceWebpage, currentElementTraits, returnElement=True)
        await logInElements["logInButton"].click()
        
        for currentElementType, currentElementTraits in saucePageErrorLoginObjects.items():
            if "locatorCount" in currentElementTraits:
                await checkDefaultElements(sauceWebpage, currentElementTraits, howManyLocators=2)
            else:
                await checkDefaultElements(sauceWebpage, currentElementTraits)
        
        await verifyPageTitleAndClose(sauceWebpage, saucePageTitle, browserInstance)

# To Debug in Terminal: run the following
# from playwright.sync_api import sync_playwright, expect, Locator
# playwright = sync_playwright().start()
# chromeBrowser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=100)
# newPage = chromeBrowser.new_page()
# url = "https://www.saucedemo.com/"
# newPage.goto(url)