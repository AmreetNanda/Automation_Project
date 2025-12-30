# 🧠  AI-Assisted Test Automation Framework

A Python-based **comprehensive AI-assisted test automation framework** framework for automating Android Automotive OS (AAOS) app testing using Appium, Pytest, and an AI-powered test generator. It integrates automated mobile testing using **Appium**, test execution with **Pytest**, and machine learning to predict and self-heal failing tests.

---
# 🎯 Goal
The goal of the AAOS Automated Test Runner project is to build an intelligent, end-to-end automated testing framework for AAOS (Android Automotive OS) applications that leverages AI and machine leaming to:
- Automate test creation: Convert natural language test descriptions into executable Python test scripts using an LLM-powered generator.
- Enhance test reliability: Detect Ul element failures and automatically heal broken locators to maintain test stability.
- Predict and analyze failures: Use machine learning models, such as a RandomForest, to classify and prioritize test failures for faster debugging.
- Provide real-time insights: Stream Appium and Pytest logs through a GUI for monitoring test execution and AI-driven diagnostics.
- Streamline DevOps integration: Offer Dockerized deployment and modular architecture to simplify CI/CD integration and scale testing across devices.
- This framework aims to reduce manual test effort, accelerate QA cycles, and enable more resilient automated testing for automotive applications.
---

## ✨Features

- GUI-based test runner: Manage Appium server and tests easily.
- AI Test Generator: Generate Python test scripts from natural language prompts.
- ML-based failure prediction using **RandomForestClassifier**.
- Self-healing tests for resilient automated testing.
- Real-time Logs: Appium logs (green) and Pytest logs (red) in GUI.
- Reporting: HTML reports for test execution.
- Screenshots on failure: Automatically captures screenshots when tests fail.
- Fully integrated end-to-end automation workflow with NLP + GUI codebase
- This framework allows you to:
  - Start and stop an Appium server from a GUI
  - Select and run pre-defined or AI-generated tests
  - Generate real-time test logs for Appium and Pytest
  - Generate AI test cases from natural language prompts
  - Automatically register AI-generated tests for future runs
  - Run tests inside Docker using a fully reproducible environment

## 🧰Requirements

- Docker & Docker Compose (for containerized execution)
- Python 3.11+
- Node.js (for Appium server)
- Android device or emulator with USB debugging enabled
Optional:
- Internet connection for AI test generation (if using OpenAl API or other AI service)

## 🏗 Architecture 
   - **Test Execution**: Pytest runs tests on Appium-controlled devices.
- **Machine Learning**:  
   - **RandomForest** predicts potential test failures from historical logs.  
   - Failure logs are analyzed, and locators are patched automatically.
-  **AI Test Generation**: Natural language prompts are converted to executable test scripts.
-  **GUI Interface**: Tkinter-based dashboard for running tests, monitoring logs, and opening reports.

## Project Structure
```bash
AAOS_Automation/
│
├── ai/                                         # LLM + Orchestration Layer
│ ├── logs/                                  
│ ├── init.py
│ ├── ai_refactor.py							# Refactor generated test code
│ ├── code_normalizer.py						# Normalize AI generated code formating
│ ├── code_sanitizer.py							# Clean up un-safe code and syntax issues
│ ├── failure_analyzer.py						# ML powered failure classifier and report generation
│ ├── failure_pattern_miner.py					# Extract common failure pattern from logs
│ ├── healing_logger.py						    # Logs Self-healing events
│ ├── intent_engine.py							# Interprets user prompts for test generation
│ ├── locator_generator.py						# Suggest alternate locators for failed elements
│ ├── ollama_client.py                          # Client for LLM 
│ ├── prompts.py								# predefined prompt for test generation
│ ├── registry_updater.py                       # Auto register AI generated test cases
│ ├── self_healing.py							# Extract + heal failed locators
│ ├── test_patcher.py							# Patches test code with healed locators
│ └── test_generator.py			                # AI test generation Logic (NLP)
│
├── config/ 
│ ├── init.py
│ └── capabilities.py                           # configuration of the andriod or AAOS device
│
│
├── ml/ 										# ML models and data processing layers
│ ├── init.py
│ ├── data/										# Data collection and dataset management 
│ │   ├── processed/
│ │   ├── raw/
│ │   ├── collector.py							# Collect logs and events for training
│ │   ├── dataset.py							# Manage training datasets
│ │   ├── locator_dataset.py					# Dataset specifically for locator reliability
│ │   ├── locator_event.py						# Track locator usage events
│ │   └── schemas.py							# Data schemas for ML processing
│ │ 
│ ├── features/   							
│ │   └── log_features.py           			
│ │       
│ ├── inference/
│ │   └── locator_ranker.py						# Rank locators based on reliability
│ │ 
│ ├── models/    
│ │   ├── failure_classifier.py					# ML classifier for test failure classification
│ │   ├── labels.py							
│ │   └── locator_reliability.py 				# ML based locator reliability scoring 
│ │ 
│ ├── training/       
│ │   └── training_locator_model.py				# Train locator reliability model
│ │ 
│ └── metrics                        
│
├── framework/ 
│ ├── init.py
│ └── test_registry.py                          # Pre-defined testcase registry (Manual + AI)
│
├── tests/ 
│ ├── init.py
│ ├── test_ai_*.py                              # Auto generated AI test scripts
│ └── Manual_written_testcases*.py              # Pre-written test scripts (Manual)
│
├── ui/ 
│ ├── init.py
│ ├── ai_panel.py   							# (Optional) AI panel module
│ └── runner_gui.py                             # Tkinter GUI for running tests                      
│
├── utils/ 
│ ├── init.py
│ ├── driver_setup.py							# Appium driver setup/teardwon
│ ├── appium_server.py                          # Appium server wrapper
│ ├── port_checker.py                           # Check port availability
│ ├── element_finder.py							# Safe element lookup for Appium
│ ├── locator_logger.py							# Logs locator usage
│ └── safe_finder.py                            # Safer element search with fallback
│
├── Dockerfile                                  # Docker container
├── docker-compose.yml 
├── requirements.txt                            # Python dependencies
├── run.py 										# Running the app
└── README.md 
```

### 🧠 How the App Works for pre-registered (Manual) testcases 
```bash
1. Start the Appium server from the GUI.
2. Select pre-registered test cases.
3. Run tests and view live logs.
4. Failed tests are automatically analyzed and retried if self-healing is successful.
5. Open HTML reports after execution.
```

### 🧠 Generating AI testcases and running it in GUI
```bash
1. Start the Appium server from the GUI.
2. Navigate to the AI Test Generator tab in the GUI.
3. Enter a test description in natural language, for example "Test Google Maps: Open app, search for coffee shops, verify results list"
4. Click Generate & Run Test button.
5. The generated test will be automatically registered in the dropdown for future execution.
6. Select AI generated test cases.
7. Run tests and view live logs.
8. Failed tests are automatically analyzed and retried if self-healing is successful.
9. Open HTML reports after execution.
```

### ML Component
**Model**: RandomForestClassifier
**Input Features**: Test logs, failed locators, error types, execution context.
**Functionality**:
- Predicts test failures before execution.
- Provides insights for self-healing mechanism.
- Improves automation reliability and reduces manual debugging.

## Installation

## 🛠 Installation (without Docker)

### 1. Clone the repo
```bash
git clone https://github.com/AmreetNanda/Automation_Project.git
cd AAOS_Automation/
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Appium 
```bash
npm install -g appium
```

### 3. Runing the GUI
```bash
python ui/run.py
```
👉 Open the app window for further operations
 

## 🐳 Running with Docker (optional)
### Build and run the container
```bash
docker-compose up --build
```
- appium: Starts the Appium server.
- tests: Executes pytest tests and generates an HTML report

### Access Report 
The HTML report is saved in 
- reports/test_report.html

Open it in a browser
```bash
Open: 👉 reports/test_report.html
```

### Troubleshooting
- Appium button not found: Ensure Google Maps is installed and accessible on the device/emulator.
- Docker issues: Make sure the device/emulator is connected and accessible from Docker.
- AI test generation errors: Check internet connection and AI API keys (if applicable).
- KeyError when running tests: Ensure AI-generated tests are registered using the registry.

## Screenshots
### GUI 
![App Screenshot](https://github.com/AmreetNanda/Automation_Project/blob/main/GUI.png)

### AI test generator Tab 
![App Screenshot](https://github.com/AmreetNanda/Automation_Project/blob/main/AI%20Test%20Generator%20Tab.png)

### Failure Analysis if failed - 1 
![App Screenshot](https://github.com/AmreetNanda/Automation_Project/blob/main/Failure%20Analysis%20-%201.png)

### Failure Analysis if failed - 2 
![App Screenshot](https://github.com/AmreetNanda/Automation_Project/blob/main/Failure%20Analysis%20-%202.png)

## Demo 
https://github.com/user-attachments/assets/5049d423-4334-4fa4-ab06-a786c3d31d82

## License
[MIT](https://choosealicense.com/licenses/mit/)