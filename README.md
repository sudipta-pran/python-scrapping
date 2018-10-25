# Web Scrapping using Python and Beautiful Soup

This project was actually tested on a production server but the URL has been changed here

## Python 3.7.1

Download latest version of python. This project was performed on windows 10 machine, which needs PATH to be set

## Pip version 18.1

If Pip is not the latest version when you install python, upgrade it.

## Beautiful Soup

Run `pip3 install bs4` to install Beautiful Soup

## About this project

This script was run on a site that listed its client companies (about 1100+) in a paginated webpage. Again each company had its own page where their details could be found. If a human copies and pastes all that information on an excel sheet, it will take many days!!!

This script iterates over items, scraps the page link and scrapes that individual page in a separate function. Then returning to the scrapping, it continues this process till all items are scraped. Then it goes to the next page, using reccursion on that function and the whole process continues. Once a page has no items, it returns an empty array where the reccursion breaks.

There are additional problems on windows. Mainly the UTF encoding is explicitly required while writing to a csv file. There may be empty alternate rows, so specify `newline = ''`. Then maybe due to computer hardware limitations, script stops midway with no0 response from server message. Try it on some site with less items to scrape.

Good Luck!!!

## Further help

To get more help on this project contact at ('http://www.jinsoft.in')