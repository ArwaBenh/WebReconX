<h1 align="center">🔍 WebReconX</h1>
<p align="center">
  <i>Website Information Scanner — Built with Python</i>
</p>

<p align="center">
  <img src="DEMO.gif" alt="WebReconX Demo" width="80%">
</p>

---

## 🚀 What is WebReconX?

**WebReconX** is a terminal-based Python tool to scan websites and gather useful public information like WHOIS, IP address, `robots.txt`, `sitemap.xml`, and more — presented in a clean and colorful output using `rich` and `pyfiglet`.


---

## 🚀 Features

- ✅ Fetches domain WHOIS info (registrar, created/updated/expires)
- 🌍 Resolves IP address from domain
- 📄 Shows key HTTP headers
- 🗺️ Reads sitemap.xml (if exists)
- 🤖 Parses robots.txt
- 👨‍💻 Displays humans.txt, ads.txt, and security.txt
- 💾 Saves a full report to a `.txt` file
- 🎨 Beautiful terminal output using `rich` and `pyfiglet`

---
## 🛠 Installation & Usage

1. Clone the repository:
<pre>
git clone https://github.com/ArwaBenh/WebReconX.git
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
## ✅ Requirements

* Python 3.7+
* `requests`
* `rich`
* `pyfiglet`
---
## 📂 Output

<p>If enabled, results will be saved to: data-saved(WebReconX).txt</p>

---
## ⚠️ Legal Disclaimer

This tool is intended for educational and authorized security research purposes only.
It collects only publicly accessible data (like robots.txt, security.txt, headers, etc.).

<p>Don't use it on websites you don't own or don't have explicit permission to scan</p>

---
## 📄 License

This project uses only public APIs and gathers public information legally. Please use responsibly.

---

