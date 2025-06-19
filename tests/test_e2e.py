from playwright.sync_api import Page, expect
from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page


def test_index_page(page: Page, live_server_url: str):
    """Test that the index page loads correctly."""
    page.goto(f"{live_server_url}index.html")
    
    # Expand the first unit in the sidebar
    page.get_by_role("button", name="Python Fundamentals").click()
    page.get_by_role("link", name="Values & Expressions", exact=True).click()
    page.locator("code-exercise-element[name=magic-birthday-math]").get_by_label("Run code").click()
    expect(page.locator("code-exercise-element[name=magic-birthday-math] ")).not_to_contain_text("Running code")
    expect(page.locator("code-exercise-element[name=magic-birthday-math] pre code")).to_contain_text("7")

    # Check inline quiz
    page.get_by_role("main").get_by_role("link", name="Nested Call Expressions", exact=True).click()
    page.get_by_role("radio", name="Yes, there needs to be an import statement above it.").check()
    page.locator("form").filter(has_text="🧠 Check Your Understanding Is any additional code required for the above call").get_by_role("button").click()
    expect(page.locator("#content")).to_contain_text("This answer is correct, there needs to be from operator import add before this line of code.")
    
    # Check code exercise with doctests
    page.get_by_role("link", name="Exercise: Functions").click()
    page.locator("code-exercise-element[name=lifetime-supply-calculator]").get_by_label("Run tests").click()
    expect(page.locator("code-exercise-element[name=lifetime-supply-calculator]")).not_to_contain_text("Running code")
    expect(page.locator("code-exercise-element[name=lifetime-supply-calculator]")).to_contain_text("❌ Failed test: calculate_lifetime_supply(99, 1) Expected: 365 Got nothing")


def test_next_links(page: Page, live_server_url: str):
    """Test that the next links work correctly by following all next links until Project 4."""
    page.goto(f"{live_server_url}index.html")
    
    # Click on link with text "Jump into the first unit!"
    page.get_by_role("link", name="Jump into the first unit!").click()
    expect(page).to_have_url(f"{live_server_url}1-python-fundamentals/0-unit-overview.html")

    # Initialize counters for tracking progress
    visited_pages = set()
    current_url = page.url
    visited_pages.add(current_url)
    
    # Track progress through units
    unit_progress = {
        "1-python-fundamentals": False,
        "2-loops-&-lists": False,
        "3-strings-&-dictionaries": False,
        "4-object-oriented-programming": False
    }
    
    # Follow next links until we reach Project 4 or hit a cycle
    max_clicks = 100  # Safety limit to prevent infinite loops
    clicks = 0
    
    while clicks < max_clicks:
        # Check if we've reached Project 4
        if "4-object-oriented-programming/12-project-4-oop-quiz.html" in page.url:
            print("Successfully reached Project 4!")
            # Verify it's the final project
            expect(page.locator("h1")).to_contain_text("Project 4:")
            break
        
        # Check which unit we're in
        for unit in unit_progress.keys():
            if unit in page.url:
                unit_progress[unit] = True
        
        # Look for next-step section with link
        next_link = page.locator("section.next-step").get_by_role("link")
        
        # If no next link or it's not visible, we've hit a dead end
        if next_link.count() == 0:
            raise AssertionError(f"No next link found on page {page.url}")
        
        # Click the next link
        with page.expect_navigation():
            next_link.click()
        
        # Verify navigation worked and we're on a valid page
        expect(page.locator("main h1")).to_be_visible()
        
        # Check if we've already visited this page (cycle detection)
        current_url = page.url
        if current_url in visited_pages:
            raise AssertionError(f"Cycle detected! Revisited page: {current_url}")
        
        visited_pages.add(current_url)
        clicks += 1
        print(f"Navigated to: {page.url}")
    
    # Verify we visited all units
    for unit, visited in unit_progress.items():
        assert visited, f"Failed to visit any page in unit {unit}"
    
    # Make sure we didn't hit the safety limit
    assert clicks < max_clicks, f"Hit safety limit of {max_clicks} clicks without reaching Project 4"



def test_a11y(page: Page, live_server_url: str):
    axe = Axe()
    page.goto(f"{live_server_url}/index.html")
    results = axe.run(page)
    assert results.violations_count == 0, results.generate_report()