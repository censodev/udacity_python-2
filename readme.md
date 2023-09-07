# Meme Generator

A multimedia application to dynamically generate memes.

## Setup

Install dependencies:

```cmd
pip install -r requirements.txt
```

## Usages

### Web

```cmd
py src/app.py
```

Access the web application at <http://127.0.0.1:5000>

### CLI

Generate meme randomly:

```cmd
py src/meme.py
```

Generate meme manually:

```cmd
py src/meme.py -p "<IMAGE_PATH>" -b "<QUOTE_BODY>" -a "<QUOTE_AUTHOR>"
```

```cmd
py src/meme.py --path="<IMAGE_PATH>" --body="<QUOTE_BODY>" --author="<QUOTE_AUTHOR>"
```
