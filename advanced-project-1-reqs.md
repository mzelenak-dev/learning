# Mini Project: Smart String Analyzer CLI
___

## Concept Recap:
### This project builds on:
    - Functions (with parameters & return values)
    - String and number manipulation
    - Type conversion
    - f-strings with formatting
    - Escape characters (\n, \t)
    - Local vs. global scope
    - Thinking through flow and logic

## Project Scenario
    You're building a CLI tool (Command Line Interface) for engineers who copy/paste raw text logs. Your tool analyzes a log string and summarizes it with helpful metrics.

## Requirements
    - Ask the user to input a log string (can be multi-word, even with numbers).
    - Build a function analyze_log(log) that:
    - Returns the number of characters and words in the log.
    - Counts how many numeric characters (0–9) appear.
    - Returns whether the string is entirely uppercase, lowercase, or mixed.
    - Returns a formatted report using \n and \t with all the results.
    - Create another function clean_and_analyze(log, convert_case="none"):
    - If convert_case="lower", convert log to lowercase before analysis.
    - If convert_case="upper", convert log to uppercase before analysis.
    - Use this to demonstrate parameter defaults + overrides.
    - Demonstrate that a global variable (e.g., status = "raw") does not interfere with a local status variable inside a function.

## Sample Output
`Enter log string: TEMP HIGH @ 88C SENSOR 2`
``
`Analysis Report:`
`    Characters: 26`
`    Words: 5`
`    Numeric digits: 3`
`    Case: UPPER`
``
`Modified (lower) Analysis:`
`    Characters: 26`
`    Words: 5`
`    Numeric digits: 3`
`    Case: lower`


## Bonus Challenge (optional)
    Let the user decide whether to run the lower/upper analysis by entering "y" or "n"—this adds a conditional logic twist!