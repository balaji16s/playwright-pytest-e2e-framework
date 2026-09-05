# Playwright Pytest E2E Framework

A scalable end-to-end (E2E) test automation framework built with **Playwright**, **Python**, and **pytest**, designed for testing both **UI** and **API** layers together. It comes with a Page Object Model setup, API-driven test data handling, centralized configuration, and reporting — everything you need as a starting point for a real, growing test suite.

---

## What's in the Box

- **UI testing** with Playwright (Chromium, Firefox, WebKit)
- **API testing** using Playwright's built-in request capabilities
- **Hybrid tests** — use the API to set up data fast, then verify the actual feature through the UI
- **Page Object Model** structure to keep locators and page logic reusable
- **Centralized config** via `.env` and `config/settings.py` — no hardcoded URLs or credentials
- **Test data management** kept separate from test logic
- Built to plug into CI/CD pipelines

---

## Project Structure

```
playwright-pytest-e2e-framework/
├── pages/              # Page Object classes — reusable representations of UI pages
├── api/                # Reusable API request logic
├── tests/
│   ├── ui/             # UI-only tests
│   ├── api/            # API-only tests
│   └── e2e/            # End-to-end tests that combine UI and API together
├── fixtures/           # Shared setup/teardown logic used across tests
├── config/             # Centralized settings (URLs, timeouts, etc.)
├── utils/              # Helper functions and shared utilities
├── data/               # Test data files (JSON, CSV, YAML, etc.)
├── reports/            # Generated test reports (not committed to git)
├── conftest.py         # Shared pytest fixtures available to all tests
├── pytest.ini          # Pytest configuration and markers
├── requirements.txt    # Python dependencies
├── .env                # Local environment values (not committed to git)
└── README.md
```

If you're new to this project, this is the fastest way to understand what lives where — start in `tests/` to see what's actually being tested, and use `pages/`, `api/`, and `fixtures/` to see how those tests are supported behind the scenes.

---

## Before You Start

Make sure you have these installed on your machine:

- **Python 3.10+** — [Download Python](https://www.python.org/downloads/)
- **Git** — [Download Git](https://git-scm.com/downloads)

You don't need to install any browsers manually — Playwright handles that for you in the setup steps below.

---

## Getting Started

Follow these steps in order. Each one builds on the last, so try not to skip ahead.

### 1. Clone the repository

```bash
git clone https://github.com/balaji16s/playwright-pytest-e2e-framework.git
cd playwright-pytest-e2e-framework
```

This downloads a copy of the project to your machine and moves you into the project folder.

### 2. Create a virtual environment

```bash
python -m venv venv
```

A virtual environment keeps this project's Python packages separate from everything else on your machine, so nothing conflicts with other projects you might have.

Activate it:

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

You'll know it worked if you see `(venv)` at the start of your terminal prompt.

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

This installs everything the framework needs — Playwright, pytest, the pytest-playwright plugin, and a few supporting libraries.

### 4. Install the browsers

```bash
playwright install
```

Playwright uses its own dedicated browser binaries (Chromium, Firefox, WebKit) rather than the ones already on your computer. This one-time step downloads them, and makes sure tests behave the same way on every machine that runs them.

### 5. Set up your environment file

Copy the example file and fill in your own values:

```bash
cp .env.example .env
```

Open `.env` and set values like:

```
BASE_URL=https://your-app-url.com
API_BASE_URL=https://your-api-url.com
```

This file holds settings specific to your local setup (or environment), and it's never committed to git — so URLs, credentials, or tokens stay off of GitHub.

---

## Running Tests

Once you've completed the setup above, you're ready to run tests.

**Run everything:**
```bash
pytest
```

**Run only UI tests:**
```bash
pytest -m ui
```

**Run only API tests:**
```bash
pytest -m api
```

**Run only hybrid (UI + API) tests:**
```bash
pytest -m e2e
```

**Run tests and see print statements / logs in the terminal:**
```bash
pytest -v -s
```

**Run tests in parallel (faster, once you have several tests):**
```bash
pytest -n auto
```

---

## Viewing Reports

After a test run, an HTML report is generated in the `reports/` folder. Open it in a browser to see a readable breakdown of what passed, what failed, and why.

---

## How This Framework Is Organized (In Plain Terms)

- **`pages/`** exists so that if a button or field on a page changes, you fix it in **one place**, not in every test that uses it.
- **`api/`** keeps your API calls (like login or creating test data) reusable, instead of copy-pasting request code into every test.
- **`fixtures/`** holds setup and cleanup logic that multiple tests share — for example, logging in once and reusing that session across several tests.
- **`config/`** and **`.env`** work together so the same tests can run against different environments (local, staging, production) just by changing one file.
- **`data/`** keeps test inputs separate from test logic, so updating test data doesn't mean touching test code.

The goal of this structure is simple: anyone opening this repo for the first time — including future-you — should be able to understand where things live without needing an explanation.

---

## Contributing

If you're working on this alongside others:

1. Create a new branch off `develop` for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and commit them with a clear message.
3. Push your branch and open a pull request back into `develop`.

Keeping `main` and `develop` stable means new work always happens on its own branch first.

---

## License

This project is open for learning and personal use. Feel free to fork it and adapt it for your own testing needs.