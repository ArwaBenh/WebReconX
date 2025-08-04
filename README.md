![Screenshot](screenshot.png)

## WebReconX

**WebReconX** is a simple, legal, and shareable command-line Python tool for scanning website information including WHOIS data, IP address, HTTP headers, and more.

---

## Features

* Fetches WHOIS domain info (registrar, creation, expiration dates)
* Resolves domain IP address
* Shows important HTTP response headers
* Saves report to a text file if requested
* Pretty terminal output using `rich` and ASCII banner with `pyfiglet`

---
## Installation & Usage

1. Clone the repository:
<pre>
git clone https://github.com/yourusername/WebReconX.git
</pre>
2.  Navigate to the project folder:
<pre>
cd WebReconX
</pre>
3.  Install required Python packages:
<pre>
pip install requests rich pyfiglet
</pre>
4.  Run the tool with a URL:
<pre>
python webreconx.py --url https://example.com
</pre>
Replace https://example.com with the website you want to scan.

---
## Requirements

* Python 3.7+
* `requests`
* `rich`
* `pyfiglet`

Install dependencies with:

```bash
pip install requests rich pyfiglet
```

---

## License

This project uses only public APIs and gathers public information legally. Please use responsibly.

---

