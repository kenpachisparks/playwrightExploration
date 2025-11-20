# Objects on the Main Example.com Page

exampleUrl = "https://www.example.com"

exampleDefaultObjects = {
    # Need to use Regex for this heading for more accurate locations due to a shared heading name for Example and Learn More pages
    "heading": {"htmlType": "h1", "has_text": "Example Domain", "textCheck": "Example Domain"},
    "description": {"htmlType": "p", "has_text": "This domain is for use in documentation examples without needing permission. Avoid use in operations."},
    "learnMore": {"htmlType": "a", "locatorType": "href", "locatorText" : "https://iana.org/domains/example", "textCheck": "Learn more"}
}

exampleHeading = exampleDefaultObjects["heading"]
exampleHDescription = exampleDefaultObjects["description"]
exampleLearnMode = exampleDefaultObjects["learnMore"]

examplePageTitle = exampleHeading["has_text"]
