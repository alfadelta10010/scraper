# scraper

A Simple Selenium based program that works on scraping student data from PESU Academy for the [PES25 Bot](https://github.com/alfadelta10010/pesu-bot-2025)

## Usage

```bash
  cd scraper/
  source scrapeEnv/bin/activate
  python3 scraper <rr or ec> <year>
```

## Tech stack

Seleniun, Python

## How it works

The scraper goes to PESU Academy, uses the `Know your section` tool, and enters a PRN. Once done, it sends that, and copies details from the result table. Saves it to a SQL Database.
