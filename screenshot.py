import click

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@click.command()
@click.option('--user', default='', help='User Login')
@click.option('--pwd', default='', help='pwd')
def main(user, pwd):
    driver = webdriver.Firefox()
    driver.get("http://www.tradingview.com")
    # continue_link = driver.find_element_by_link_text('Continue')
    # continue_link = driver.find_element_by_partial_link_text('Conti')
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


if __name__ == '__main__':
    main()

