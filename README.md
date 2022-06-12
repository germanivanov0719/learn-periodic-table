> **C++ Edition is no longer maintained, and will be archived soon.**

# Learn Periodic Table CLI (Python Edition)

This simple CLI program can help you memorize Periodic table easily using help of your computer.
It has customizable choice of elements (by groups), and allows you to:
1. Learn elements on-by-one (just scroll through them).
2. Check your knowledge of either names or symbols (you will have to type them as you remember).

This app uses ASCII escape sequences to paint characters in the terminal. Without their support, just change them to empty strings in [`console_resources/colored_output.py`](console_resources/colored_output.py)

## Resources

Table resources are stored as a Python dictionary in [`table/periods_resource.py`](table/periods_resource.py). Feel free to use them with your projects. <br />
Unfortunately, only Russian names are avaliable for now, but English is expected to be added soon.

## License

MIT License
