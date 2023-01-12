# html2json-parser-ex1
Program to parse HTML to json data object

## Dependencies
1. BeautifulSoup
2. `lxml` HTML Parser

## Setup

`pip install -r requirements.txt`

## Example

`python main.py index.html`

### Output

A file named `json_output.json` stored in the parent directory of `main.py`.

```python
{
 "capitals": [
  {
   "capital": "Lansing",
   "state": "Michigan"
  },
  {
   "capital": "Sacramento",
   "state": "California"
  }
 ],
 "summary": {
  "numberOfCapitals": 2
 }
}
```
