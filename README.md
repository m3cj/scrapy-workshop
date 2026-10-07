# Web Scraping Tutorials & Slides

Scrapy starter projects and presentation slides for learning and demonstrating web scraping.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running Spiders

1. **Basic Spider**:
   ```bash
   cd tutorials/01_basic_spider
   scrapy crawl quotes
   ```

2. **Items & SQLite Pipeline**:
   ```bash
   cd tutorials/02_items_and_pipelines
   scrapy crawl quotes
   ```

3. **Starter Template**:
   ```bash
   cd tutorials/03_demo_template
   scrapy crawl example
   ```

## Presentation

Presentation slides are located in `presentations/scrapyPPT.pptx`.
