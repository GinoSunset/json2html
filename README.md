JSON2HTML
===============
project to generate html from json. By default, the script searches for the source file in its source.json and sends data from it to the converter. The result is a file `index.htm`l in which title is recorded in the `h1` tag, and body is recorded in the `p` tag

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
```
python3 -s my_json.json -o result.html
```

