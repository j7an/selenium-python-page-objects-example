from behave import fixture, use_fixture
from browser import Browser
from features.pages.home_page import HomePage
from features.pages.search_results_page import SearchResultsPage


@fixture
def browser(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.search_results_page = SearchResultsPage()
    yield context.browser
    context.browser.quit()


def before_all(context):
    use_fixture(browser, context)

