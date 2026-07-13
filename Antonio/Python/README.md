# News Bot

A simple Python script that retrieves and displays news headlines from a specified website.

## Author

Antonio Paine

## Description

The News Bot script connects to a website, downloads its HTML content, and extracts news headlines using the Requests and BeautifulSoup libraries.

This project was created as part of GitHub learning and Python experimentation.

## Features

- Download web page content
- Parse HTML data
- Extract news headlines
- Simple command-line execution
- Easy to modify and extend

## Requirements

Python 3.x

Required packages:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script from a command prompt or terminal:

```bash
python news_bot.py "url"
```

## Examples

```bash
python news_bot.py "https://www.cbc.ca"
```

```bash
python news_bot.py "https://www.reuters.com"
```

```bash
python news_bot.py "https://www.cnn.com"
```

## Parameters

| Parameter | Description |
|------------|------------|
| url | Website URL containing news content |

## Example Output

```text
Top Headlines

1. Example Headline One
2. Example Headline Two
3. Example Headline Three
```

## Project Structure

```text
Antonio/
└── Python/
    ├── README.md
    └── news_bot.py
```

## Notes

This repository is used for learning:

- GitHub
- Git commits
- Repository organization
- Python scripting
- Markdown documentation

## License

For educational and testing purposes only.
