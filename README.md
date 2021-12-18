# Test github actions

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Testing github actions

**The functional checks are written in the xls file**

### Built With

* Python
* Selenium Webdriver

<!-- GETTING STARTED -->
## Getting Started
The automation script are divided by the following folders:
- config: Where general configuration as name, email, url is stored
- pages: Where we have the methods Specific for each url (Careers and demo) adn the general methods in the base_page.py
- tests: Where the test cases for each url page are present

### Prerequisites

Before running any script, the following libraries must be installed:

* Pytest: Used for better script style

`pip install -U pytest`

* **pytest-html-reporter**: Pytest plugin to generate HTML reports

`pip install pytest-html-reporter`

* **webdriver-manager**: Provides a way to automatically manage drivers for different browsers

`pip install webdriver-manager`

* **Selenium:** Python bindings for Selenium

`pip install selenium`

### Environment preparation

The script was made using Chrome Browser. To use with other browsers (Firefox and Edge) do the following steps:

1. Access the /tests folder
2. Open conftest.py
3. Comment and uncomment the lines related to the desired browser (Lines 11, 12 and 13)
   ```python
    general_driver = webdriver.Chrome(ChromeDriverManager().install())
    general_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    general_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
   ```
4. Save


<!-- USAGE EXAMPLES -->
## Usage

1. To run all the tests
`pytest tests/`
2. To run an expecific test suite
`pytest tests/desired_test.py`
3. To run an expecific test case
`pytest tests/desired_test.py::ClassName::method_name`

_For more examples, please refer to the [Documentation](https://docs.pytest.org/en/stable/usage.html)_

------------------------------------------------

* Reports will be saved in the report folder

* Open the report.html with a browser to see the full report

* To export the test results to another format click here:

![Product Name Screen Shot][product-screenshot]


[product-screenshot]: images/screenshot.png
