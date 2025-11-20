from ObjectModels.HomePageObjects import *
from Helpers.PlaywrightHelpers import *
from playwright.async_api import async_playwright

import pytest

@pytest.mark.asyncio
async def test_googleTestAutomationSearchFlow():
    async with async_playwright() as openPlaywright:
        browserInstance = await openPlaywright.chromium.launch(channel="chrome", headless=False)
        # Placeholder for now
