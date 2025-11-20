# Objects on the Sauce Page
saucePageTitle = "Swag Labs"

sauceUserName = "standard_user"
saucePassword = "secret_sauce"


sauceUrl = "https://www.saucedemo.com/"

saucePageBeforeLoginObjects = {
    "heading": {"htmlType": "div", "locatorType": "class", "locatorText" : "login_logo"},
    "logInBox": {"htmlType": "div", "locatorType": "class", "locatorText" : "login-box"},
    "userNameField": {"htmlType": "input", "locatorType": "id", "locatorText" : "user-name"},
    "passwordField": {"htmlType": "input", "locatorType": "id", "locatorText" : "password"},
    "logInError": {"htmlType": "div", "locatorType": "class", "locatorText" : "error-message-container"},
    "logInButton": {"htmlType": "input", "locatorType": "id", "locatorText" : "login-button"}
}

saucePageErrorLoginObjects = {
    "xCircle": {"htmlType": "svg", "locatorType": "class", "locatorText" : "svg-inline--fa fa-times-circle fa-w-16 error_icon", "locatorCount": 2},
    "logInError": {"htmlType": "div", "locatorType": "class", "locatorText" : "error-message-container error", "textCheck": "Epic sadface: Username is required"}
}

successfulLogInObject = {"htmlType": "div", "locatorType": "id", "locatorText" : "shopping_cart_container"}