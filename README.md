# Live Data Reporter

**Live Data Reporter** is a terminal-based Python app that helps students explore real-time data from space missions, financial markets, and global news. It connects to public APIs and presents engaging, current information in an educational, easy-to-use way.

---

## What It Does

-  Lists astronauts currently in space and their spacecraft
-  Shows the real-time location of the International Space Station (ISS)
-  Displays either:
  - The latest IBM stock price (5-minute interval), or
  - The top 3 U.S. business headlines

---

##  Features

- Simple command-line interface with a numbered menu
- Fetches live data from multiple public APIs
- Automatically logs each request and its status
- Saves key data to text files for future use
- Uses `.env` to protect your API keys
- Easily extensible for other data types or APIs

---

##  Technologies Used

- **Python 3.x**
- **APIs Used**:
  - Open Notify API (`http://api.open-notify.org`)
  - NewsAPI (`https://newsapi.org`)
  - Alpha Vantage (`https://www.alphavantage.co`)
- **Libraries**:
  - `requests`, `json`, `time`, `os`
  - `python-dotenv` for secure API key management

---

##  How to Run the App

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/live-data-reporter.git
cd live-data-reporter