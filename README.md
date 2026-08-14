[README.md](https://github.com/user-attachments/files/31060857/README.md)
*🔎 Fact-Check Agent

An AI-powered **Fact-Check Agent** that analyzes PDF documents, extracts factual claims, verifies them using web-based evidence, and presents structured fact-checking results.

The project is built with **Python, Streamlit, and Google Gemini**, with a focus on practical Generative AI, structured outputs, and automated claim verification.

---

🚀 Features

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

🏗️ Project Architecture

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

🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core application logic |
| **Google Gemini** | AI-powered claim analysis |
| **Streamlit** | Web application interface |
| **PyMuPDF / PDF library** | PDF text extraction |
| **python-dotenv** | Environment variable management |
| **Git & GitHub** | Version control and source management |

---

📁 Project Structure

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

The application returns structured results containing information such as:

- Claim
- Verdict
- Explanation
- Supporting evidence
- Confidence / reasoning where applicable

 6. Display Results

The final results are presented through the Streamlit interface in an easy-to-read format.

---

🔑 Environment Setup

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Do not commit your `.env` file to GitHub.

The API key should remain private and should never be included directly in source code.

---

💻 Installation

1. Clone the repository

```bash
git clone https://github.com/devopeish/fact-check-agent.git
cd fact-check-agent
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:**

```bash
source .venv/bin/activate
```

 4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Configure the API key

Create the `.env` file and add:

```env
GEMINI_API_KEY=your_gemini_api_key
```

---

▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

---

📌 Example Workflow

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

🎯 Project Objectives

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

🧠 Key Learning Outcomes

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

⚠️ Limitations

Fact-checking performed by an AI system should not be considered an absolute guarantee of truth.

Potential limitations include:

- Incomplete or unavailable evidence
- Ambiguous claims
- Context-dependent statements
- Limitations of the underlying language model
- Possible errors in AI-generated reasoning

For high-stakes information, results should be independently verified using authoritative sources.

---

🔮 Future Improvements

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

🌐 Deployment

The application can be deployed using platforms that support Streamlit applications.

Before deployment, make sure the `GEMINI_API_KEY` is configured securely through the platform's environment/secrets settings rather than committing it to the repository.

---

👩‍💻 Author

Devopeish

MCA '26 | Data & AI Enthusiast

Interested in **Data Analytics, Data Engineering, Generative AI, and AI Engineering**.

---

## 📄 License

This project is intended for educational and demonstration purposes.
