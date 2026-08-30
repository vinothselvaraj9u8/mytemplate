from playwright.sync_api import Page, expect


def test_homepage_shows_mytemplate_branding(page: Page):
    """A visitor loading the homepage should see MyTemplate branding."""
    page.goto("http://127.0.0.1:5000/")

    expect(page).to_have_title("MyTemplate")
    expect(page.locator("body")).to_contain_text("MyTemplate")
