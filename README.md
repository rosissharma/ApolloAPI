# 📰 Apollo API

Apollo is an open-source news API that fetches articles from various news websites. It uses FastAPI and a custom scraper to fetch the articles and offers free access for non-commercial use. No API key is required.

## Installation

Clone the repository:

```bash
git clone https://github.com/username/news-scraper.git
cd apollo
```
Install the dependencies from the virtual environment:
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Locally
```bash
uvicorn main:app --reload
```
or
```bash
python -m uvicorn main:app --reload
```