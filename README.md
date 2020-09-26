JSON2HTML
===============
project to generate html from json. By default, the script searches for the source file in its source.json and sends data from it to the converter. The result is a file `index.htm`. Tags for html are specified as keys in json. If the json contains a list , the entire html is wrapped in `<ul>` and each element is wrapped in a `li`. if an element contains a list too, then the entire element is wrapped in `<ul>` and each sub-element in the list is wrapped in `<li>`. 

Tag name can include classes and ID. To specify a class, write it through a dot; to specify an id, write it through a grid. Like in emmet.
example: `a.active.visible#main-page` -> `<a class="active visible" id="main-page">`

REQUIREMENT
-------
* python3
* pytest (for testing)

HOW TO RUN
-----------------
* write sourece json to file `source.json` 
* run script `converter.py`
    ```
    python3 converter.py
    ```

AGRGUMENTS
----------
|name|default|description|
|----|-------|-----------|
|`-s`,`--source-file`|source file format json|source.json|
|`-o`,`--output-file`|output file format html|index.html|


TEST
--------
run pytest
```
pytest
```

EXAMPLE
-------------
Run script with source file `my_json.json` and output file `result.html`

Example json:
```json
[
    {
        "h1": "Title #1",
        "content": [
            {
                "h4.active#content-1": "sub-conten"
            },
            {
                "span.escape#span": "script escape content: <script>alert()</script>"
            }
        ]
    },
    {
        "h2": "Title #2",
        "span": "Hello, World 2!"
    }
]
```


```
python3 -s my_json.json -o result.html
```


result.html 
```html
<ul><li><h1>Title #1</h1><content><ul><li><h4 class="active" id="content-1">sub-conten</h4></li><li><span class="escape" id="span">script escape content: &lt;script&gt;alert()&lt;/script&gt;</span></li></ul></content></li><li><h2>Title #2</h2><span>Hello, World 2!</span></li></ul>
```
