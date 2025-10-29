# Neovoyage: AI Trip Planner

AI Trip Planner is an intelligent travel assistant that automates itinerary creation using large language models (LLMs) and structured retrieval. It takes user inputs such as destinations, dates, and preferences, and generates optimized, context-aware travel plans.

---

## Overview

This project integrates modern AI and software engineering practices to build a modular, extensible trip-planning system. It combines prompt engineering, agent-based orchestration, and external tool integration to provide accurate and customizable travel itineraries through a web interface.

---

## Features

* Streamlit-based web interface for user input and itinerary visualization
* REST-style backend architecture handling AI prompts and data retrieval
* Modular agent system for orchestrating LLM responses and external tools
* Structured prompt templates for reproducible, configurable results
* Integrated logging, exception handling, and environment management
* Support for real-time AI-generated trip itineraries
* Easily extendable with new tools or prompt templates

---

## Tech Stack

* **Language:** Python
* **Frontend:** Streamlit
* **Backend / Orchestration:** Custom agent module using prompt templates
* **AI Layer:** Large Language Models (e.g., GPT)
* **Configuration Management:** Environment files and config modules
* **Logging and Error Handling:** Custom logger and exception modules
* **Build & Packaging:** `pyproject.toml`, `setup.py`, `uv.lock`
* **Utilities:** Helper modules for parsing, data handling, and formatting

---

## Repository Structure

```
AI_Trip_Planner/
│
├── agent/                # Core logic for orchestration between tools, prompts, and LLM
├── config/               # Environment variables, constants, and model configuration
├── exception/            # Custom exception handling classes
├── logger/               # Application-wide logging utilities
├── notebook/             # Experimental or exploratory Jupyter notebooks
├── prompt_library/       # Prompt templates and context chaining logic
├── tools/                # External API connectors and retrieval functions
├── utils/                # Helper functions and shared utilities
│
├── Streamlit_app.py      # Streamlit UI entry point
├── main.py               # CLI runner for the app
├── pyproject.toml        # Build configuration
├── setup.py              # Package setup file
├── requirements.txt      # Python dependencies
├── uv.lock               # Dependency lock file
├── .python-version       # Python version specification
├── .env.name             # Environment variable template
└── README.md             # Project documentation
```

---

## Installation

### Prerequisites

* Python (version specified in `.python-version`)
* Required API keys (e.g., OpenAI, travel or place data APIs)
* Git for repository cloning

### Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/kalhar108/AI_Trip_Planner.git
   cd AI_Trip_Planner
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate       # Mac/Linux
   venv\Scripts\activate          # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:

   * Copy `.env.name` to `.env`
   * Add your API keys and configuration values

5. (Optional) Install in editable mode:

   ```bash
   pip install -e .
   ```

---

## Usage

### Running via Streamlit (UI Mode)

```bash
streamlit run Streamlit_app.py
```

Access the interface at `http://localhost:8501` in your browser.

### Running via Command Line (CLI Mode)

```bash
python main.py
```

Follow on-screen prompts to generate a trip plan via terminal.

---

## System Flow

1. User inputs destination, travel dates, and preferences.
2. The agent module processes input and selects the appropriate tools.
3. Prompt templates from `prompt_library/` are dynamically populated.
4. The AI model generates a detailed itinerary.
5. External tools fetch supporting data (locations, summaries, etc.).
6. The output is rendered via Streamlit or CLI.
7. Logging and exception handlers record execution details.

---

## Design Highlights

* Modular, decoupled architecture for easier maintenance and scaling
* Prompt-based design for reproducible and controllable AI responses
* Clean separation of interface (Streamlit) and logic (agent/tools)
* Built-in error handling and configurable logging
* Designed for reproducibility using dependency locking and env files

---

## Future Improvements

* Add live flight and hotel API integration
* Include cost estimation and budget optimization
* Map visualization for itineraries (e.g., Folium, Mapbox)
* Export itineraries as PDF or JSON
* User authentication and persistent trip history
* Cloud deployment via Docker and Railway/Render/AWS
* Comprehensive unit and integration testing

---

## Contributing

1. Fork this repository
2. Create a new branch:

   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes and push the branch
4. Open a Pull Request describing your updates

---

## License

Specify your license here (e.g., MIT, Apache 2.0).

---

## Author

**Kalhar**
GitHub: [https://github.com/kalhar108](https://github.com/kalhar108)

---

Would you like me to write a short **project description section** for the top of the README (2–3 lines, ideal for GitHub preview and search indexing)? It makes your repo look more polished.
