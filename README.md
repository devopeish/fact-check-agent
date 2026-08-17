<<<<<<< HEAD
# 🔎 Fact-Check Agent

An AI-powered **Fact-Check Agent** that analyzes PDF documents, extracts factual claims, verifies them using web-based evidence, and presents structured fact-checking results.
=======
[README.md](https://github.com/user-attachments/files/31060857/README.md)
*🔎 Fact-Check Agent

- An AI-powered **Fact-Check Agent** that analyzes PDF documents, extracts factual claims, verifies them using web-based evidence, and presents structured fact-checking results.
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

The project is built with **Python, Streamlit, and Google Gemini**, with a focus on practical Generative AI, structured outputs, and automated claim verification.

---

<<<<<<< HEAD
## 🚀 Features
=======
🚀 Features
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

- 📄 Upload PDF documents through a simple web interface
- 🔍 Extract factual claims from the uploaded document
- 🤖 Analyze claims using Google Gemini
- 🌐 Verify claims against available evidence
- ✅ Classify claims based on their verification status
- 📝 Provide explanations and supporting evidence
- 📊 Present results in a structured and readable format
- ⚡ Interactive Streamlit interface
- 🔐 API credentials managed using environment variables

---

<<<<<<< HEAD
## 🏗️ Project Architecture
=======
🏗️ Project Architecture
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

```text
                    ┌──────────────────┐
                    │   PDF Document   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Streamlit UI    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ PDF Text         │
                    │ Extraction       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Claim Extraction │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Gemini AI Model  │
                    │ Analysis         │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Fact Verification│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Structured       │
                    │ Results          │
                    └──────────────────┘
```

---

<<<<<<< HEAD
## 🛠️ Tech Stack
=======
🛠️ Tech Stack
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

| Technology | Purpose |
|---|---|
| **Python** | Core application logic |
| **Google Gemini** | AI-powered claim analysis |
| **Streamlit** | Web application interface |
| **PyMuPDF / PDF library** | PDF text extraction |
| **python-dotenv** | Environment variable management |
| **Git & GitHub** | Version control and source management |

---

<<<<<<< HEAD
## 📁 Project Structure
=======
📁 Project Structure
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

```text
fact-check-agent/
│
├── app.py                  # Streamlit application
├── fact_checker.py         # Fact-checking and AI logic
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
│
└── screenshots/            # Optional application screenshots
```

> File names may vary depending on the final project structure.

---

<<<<<<< HEAD
## ⚙️ How It Works

### 1. Upload a PDF

The user uploads a PDF document through the Streamlit interface.

### 2. Extract Text

The application extracts readable text from the uploaded document.

### 3. Identify Claims

The extracted content is analyzed to identify statements that can be treated as factual claims.

### 4. Analyze Claims

Each claim is processed using the Gemini model to determine its factual status and supporting reasoning.

### 5. Generate Results
=======
⚙️ How It Works

1. Upload a PDF

The user uploads a PDF document through the Streamlit interface.

2. Extract Text

The application extracts readable text from the uploaded document.

3. Identify Claims

The extracted content is analyzed to identify statements that can be treated as factual claims.

4. Analyze Claims

Each claim is processed using the Gemini model to determine its factual status and supporting reasoning.

5. Generate Results
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

The application returns structured results containing information such as:

- Claim
- Verdict
- Explanation
- Supporting evidence
- Confidence / reasoning where applicable

<<<<<<< HEAD
### 6. Display Results
=======
 6. Display Results
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

The final results are presented through the Streamlit interface in an easy-to-read format.

---

<<<<<<< HEAD
## 🔑 Environment Setup
=======
🔑 Environment Setup
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

<<<<<<< HEAD
**Do not commit your `.env` file to GitHub.**
=======
Do not commit your `.env` file to GitHub.
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

The API key should remain private and should never be included directly in source code.

---

<<<<<<< HEAD
## 💻 Installation

### 1. Clone the repository
=======
💻 Installation

1. Clone the repository
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

```bash
git clone https://github.com/devopeish/fact-check-agent.git
cd fact-check-agent
```

<<<<<<< HEAD
### 2. Create a virtual environment
=======
2. Create a virtual environment
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

```bash
python -m venv .venv
```

<<<<<<< HEAD
### 3. Activate the virtual environment

**Windows:**
=======
3. Activate the virtual environment

Windows:
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

```bash
.venv\Scripts\activate
```

<<<<<<< HEAD
**macOS/Linux:**
=======
macOS/Linux:**
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

```bash
source .venv/bin/activate
```

<<<<<<< HEAD
### 4. Install dependencies
=======
 4. Install dependencies
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
### 5. Configure the API key
=======
5. Configure the API key
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

Create the `.env` file and add:

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

<<<<<<< HEAD
## ▶️ Run the Application
=======
▶️ Run the Application
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

---

<<<<<<< HEAD
## 📌 Example Workflow
=======
📌 Example Workflow
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

```text
Upload PDF
    ↓
Extract Text
    ↓
Identify Factual Claims
    ↓
Analyze Claims with Gemini
    ↓
Verify / Classify Claims
    ↓
Generate Explanations
    ↓
Display Fact-Check Results
```

---

<<<<<<< HEAD
## 🎯 Project Objectives
=======
🎯 Project Objectives
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

The project demonstrates how Generative AI can be integrated into a practical application for automated fact-checking.

The main objectives are to:

- Build an AI-powered fact-checking workflow
- Work with unstructured PDF data
- Extract and process factual claims
- Use LLMs for structured analysis
- Build a usable AI application with Streamlit
- Apply secure API-key management
- Deploy and demonstrate a functional AI agent

---

<<<<<<< HEAD
## 🧠 Key Learning Outcomes
=======
🧠 Key Learning Outcomes
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

Through this project, the following concepts were explored:

- Generative AI application development
- Prompt engineering
- LLM-based text analysis
- Structured AI outputs
- PDF processing
- Python application development
- Streamlit application development
- API integration
- Environment variable management
- Git and GitHub workflows
- AI agent architecture
- Deployment of AI applications

---

<<<<<<< HEAD
## ⚠️ Limitations
=======
⚠️ Limitations
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

Fact-checking performed by an AI system should not be considered an absolute guarantee of truth.

Potential limitations include:

- Incomplete or unavailable evidence
- Ambiguous claims
- Context-dependent statements
- Limitations of the underlying language model
- Possible errors in AI-generated reasoning

For high-stakes information, results should be independently verified using authoritative sources.

---

<<<<<<< HEAD
## 🔮 Future Improvements
=======
🔮 Future Improvements
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

Possible future enhancements include:

- 🔗 Automatic retrieval of evidence from multiple trusted sources
- 📚 Source credibility scoring
- 📑 Detailed citation generation
- 📊 Fact-checking analytics dashboard
- 💾 Export results as PDF or CSV
- 🧠 Improved claim classification
- ⚡ Batch processing of multiple documents
- 🔐 Improved authentication and security
- 🌍 Support for multiple languages
- 🤖 Multi-agent fact-checking workflow

---

<<<<<<< HEAD
## 🌐 Deployment
=======
🌐 Deployment
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

The application can be deployed using platforms that support Streamlit applications.

Before deployment, make sure the `GEMINI_API_KEY` is configured securely through the platform's environment/secrets settings rather than committing it to the repository.

---

<<<<<<< HEAD
## 👩‍💻 Author

**Isha Kashyap**
=======
👩‍💻 Author

Devopeish
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129

MCA '26 | Data & AI Enthusiast

Interested in **Data Analytics, Data Engineering, Generative AI, and AI Engineering**.

---

## 📄 License

<<<<<<< HEAD
This project is intended for educational and demonstration purposes.
=======
This project is intended for educational and demonstration purposes.
>>>>>>> 55441686b571848ec66f2728f743ec5c7bfc9129
