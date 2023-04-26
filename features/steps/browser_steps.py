from behave import given, when, then, step


@step(u'I visit "{url}"')
def step_impl(context, url):
    context.home_page.navigate(url)
    assert context.home_page.get_page_title() == "PyPI · The Python Package Index"


@step("I navigate to the PyPi Home page")
def step_impl(context):
    context.execute_steps(u"""
        Given I visit "https://pypi.org"
    """)


@step('I search for "{search_term}"')
def step_impl(context, search_term):
    context.home_page.search(search_term)


@step("I am taken to the PyPi Search Results page")
def step_impl(context):
    assert context.search_results_page.get_page_title() == "Search results · PyPI"


@step('I see a search result "{search_result}"')
def step_impl(context, search_result):
    assert search_result in context.search_results_page.find_search_result(search_result)
