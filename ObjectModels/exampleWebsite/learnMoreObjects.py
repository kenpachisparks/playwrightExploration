# Objects on the Main Learn More Page
learnMorePageTitle = "Example Domains"

learnMoreUrl = "https://www.iana.org/help/example-domains"

learnMoreHeaderObject = {"htmlType": "div", "locatorType": "id", "locatorText" : "header"}
# Elements underneath are dependant on learnMoreHeaderElement for consistent locations
learnMoreHeaderObjects = {
    "logo" : {"htmlType": "div", "locatorType": "id", "locatorText" : "logo"},
    "navigation" : {"htmlType": "div", "locatorType": "class", "locatorText" : "navigation"}
}
# The Logo for the heading is broken into 2 different elements which are a child of learnMoreHeaderObjects["logo"]
learnMoreLogoObjects = {
    "link" : {"htmlType": "a", "locatorType": "href", "locatorText" : "/"},
    "image" : {"htmlType": "img", "locatorType": "src", "locatorText" : "/static/_img/2025.01/iana-logo-header.svg", "altText": "Homepage"}
}
# The Navigation Buttons to the top right of the webpage are child elements of learnMoreHeaderObjects["navigation"]
# Plus these elements appear in the footer and have the same href, hence need to utilize learnMoreHeaderObjects["navigation"] for accuracy.
learnMoreNavigationObjects = {
    "domains" : {"htmlType": "a", "locatorType": "href", "locatorText" : "/domains", "textCheck": "Domains"},
    "protocols" : {"htmlType": "a", "locatorType": "href", "locatorText" : "/protocols", "textCheck": "Protocols"},
    "numbers" : {"htmlType": "a", "locatorType": "href", "locatorText" : "/numbers", "textCheck": "Numbers"},
    "about" : {"htmlType": "a", "locatorType": "href", "locatorText" : "/about", "textCheck": "About"}
}


# Would add the other elements on this page though  would like to complete the other two more tasks
# The paragraphs links match, elements in the footer exists too
learnMoreExampleDomainsObject = {"htmlType": "h1", "textCheck": "Example Domains"}
learnMoreExampleOurPolicyRemitObject = {"htmlType": "h2", "textCheck": "Our Policy Remit"}

# All About us elements

learnMoreAboutUsPageObjects = {
    "aboutUsHeading": {"htmlType": "h1", "textCheck": "About us"},
    "aboutUsFirstParagraph": {"htmlType": "p", "textCheck": "We are responsible for coordinating some of the key elements that keep the Internet running smoothly. Whilst the Internet is renowned for being a worldwide network free from central coordination, there is a technical need for some key parts of the Internet to be globally coordinated, and this coordination role is undertaken by us."},
    "missionStatementHeading": {"htmlType": "h2", "textCheck": "Mission Statement"},
    "missionStatementFirstParagraph": {"htmlType": "p", "textCheck": "This statement describes the role of PTI:"},
    "missionStatementSecondItalicsParagraph": {"htmlType": "i", "textCheck": "PTI is responsible for the operational aspects of coordinating the Internet’s unique identifiers and maintaining the trust of the community to provide these services in an unbiased, responsible and effective manner."},
    "ourPolicyRemitHeading": {"htmlType": "h2", "textCheck": "Our Policy Remit"},
    "ourPolicyRemitFirstParagraph": {"htmlType": "p", "textCheck": "We do not directly set policy by which we operate, instead we implement agreed policies and principles in a neutral and responsible manner. Using the policy-setting forums provided by ICANN, policy development for domain name operations and IP addressing is arrived at by many different stakeholders. ICANN has a structure of supporting organisations that contribute to deciding how ICANN runs, which in turn informs how PTI is operated. The development of Internet protocols, which often dictate how protocol assignments should be managed, are arrived at within the Internet Engineering Task Force, the Internet Engineering Steering Group, and the Internet Architecture Board."},
    "ourPolicyRemitSecondParagraph": {"htmlType": "p", "textCheck": "To improve its operations, we are actively involved in outreach too. As well as in ICANN forums, we participate in meetings and discussions with TLD operators, Regional Internet Registries, and other relevant communities. We provide manned helpdesks at key meetings to allow one-to-one interaction with our community of users, such as protocol developers and operators of critical Internet infrastructure."}
}
