# SlideShare OSINT Extraction Module

A maintainable extraction module for retrieving and normalizing SlideShare search results.

---

# Features

- Multi-page extraction
- Structured JSON output
- Retry handling
- Configurable settings
- Logging
- Deduplication
- Fixture-based fallback mode
- Docker support

---

# Project Structure

```txt
app/
    main.py
    extractor.py
    parser.py
    models.py
    config.py
    logger.py

fixtures/
output/
tests/
```

---

# Installation

## Local Setup

```bash
python -m venv venv
```

Activate virtual environment:

### Windows CMD

```bash
venv\Scripts\activate
```

### PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Application

## Fixture Mode

```bash
python -m app.main --query python --pages 2 --fixture
```

## Live Mode

```bash
python -m app.main --query python --pages 2
```

---

# Output

Results are exported to:

```txt
output/results.json
```

Example:

```json
[
  {
    "title": "Python Security",
    "url": "https://www.slideshare.net/test1",
    "author": "Charbel",
    "description": "Intro to Python security concepts",
    "views": 1500,
    "upload_date": "2026-05-20",
    "page": 1,
    "extracted_at": "2026-05-24T16:35:52Z"
  }
]
```

---

# Docker

Build image:

```bash
docker build -t slideshare-extractor .
```

Run container:

```bash
docker run slideshare-extractor
```

---

# Design Decisions

- Pydantic used for schema validation and normalization
- BeautifulSoup used for HTML parsing
- Requests Session used for connection reuse
- Tenacity used for retry handling
- Environment variables used for configuration management
- Fixture-based fallback implemented due to possible dynamic rendering or anti-bot protections

---

# Assumptions and Limitations

- SlideShare HTML structure may change
- Live scraping may be rate-limited or blocked
- Fixture mode is included for deterministic extraction and testing
- Current parser targets simplified fixture structure

---

# Future Improvements

- Async extraction
- Proxy rotation
- Headless browser support
- REST API interface
- Unit and integration tests
- Metrics and observability
- Redis caching
- CI/CD pipeline
- Dynamic parser selectors

---

# Running Tests

```bash
pytest
```

# Engineering Considerations

The implementation focuses on:

- Maintainability
- Separation of concerns
- Error handling
- Resiliency
- Scalability
- Production-readiness
