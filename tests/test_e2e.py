from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page


def test_index_page(page: Page, live_server_url: str):
    """Test that the index page loads correctly."""
    page.goto(f"{live_server_url}index.html")
    
    # Check basic code element
    page.get_by_role("link", name="Values & Expressions", exact=True).click()
    page.locator("code-exercise-element[name=magic-birthday-math]").get_by_label("Run code").click()
    expect(page.locator("code-exercise-element[name=magic-birthday-math] ")).not_to_contain_text("Running code")
    expect(page.locator("code-exercise-element[name=magic-birthday-math] pre code")).to_contain_text("7")

    # Check inline quiz
    page.get_by_role("link", name="Nested Call Expressions").click()
    page.get_by_role("radio", name="Yes, there needs to be an import statement above it.").check()
    page.locator("form").filter(has_text="🧠 Check Your Understanding Is any additional code required for the above call").get_by_role("button").click()
    expect(page.locator("#content")).to_contain_text("This answer is correct, there needs to be from operator import add before this line of code.")
    
    # Check code exercise with doctests
    page.get_by_role("link", name="Exercise: Functions").click()
    page.locator("code-exercise-element[name=lifetime-supply-calculator]").get_by_label("Run tests").click()
    expect(page.locator("code-exercise-element[name=lifetime-supply-calculator]")).not_to_contain_text("Running code")
    expect(page.locator("code-exercise-element[name=lifetime-supply-calculator]")).to_contain_text("❌ Failed test: calculate_lifetime_supply(99, 1) Expected: 365 Got nothing")


def test_a11y(page: Page, live_server_url: str):
    axe = Axe()
    page.goto(f"{live_server_url}/index.html")
    results = axe.run(page)
    assert results.violations_count == 0, results.generate_report()