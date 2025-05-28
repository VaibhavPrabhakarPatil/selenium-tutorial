import pytest
from py.xml import html

@pytest.fixture() # fixture function argument pass
def setup():
    print("this will run first")
    yield # yield means end function run
    print("this will run in the end")

# Html Reports Like title,url,json,summary,prefix,postfix etc.
def pytest_html_report_title(report):
    report.title = "My Very own title!"

def pytest_html_results_summary(prefix, summary, postfix):
    # Prefix: Report custom message start position
    prefix.extend([
        html.p("👨‍💻 Test executed by: Vaibhav"),
        html.p("📊 Summary of Selenium Tutorial Tests")
    ])

    # Postfix: Report last message position
    postfix.extend([
        html.p("📄 End of Report. All rights reserved © 2025.")
    ])

