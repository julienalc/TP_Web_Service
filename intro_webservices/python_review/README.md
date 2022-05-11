## Python review
The goal of this exercice is reading a local json data file and extract its content into a DataFrame

The following need to be done:
- Read the JSON file
- Parse the JSON (with the json library)
- Extract the data and store in a list of dictionaries with the following keys "firstname", "lastname", "address", "age", "job"
Example:
```python
data = [
    {
        "firstname": "Jean-Loïc",
        "lastname": "De Jaeger",
        "address": "3804 Quiet Valley Lane North Hollywood 91601",
        "age": 31,
        "job": "Software Developer"
    },
    {},
    {}
]
```
- Create a data frame from the list of dictionary
- Show the dataframe

Your code should be pushed in the right branch under your own folder just like the "dejaeger" folder