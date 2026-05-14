 Medi Scan AI

AI-powered healthcare diagnosis system built using Python, Streamlit, SQLite, and ReportLab.
Medi Scan AI analyzes symptoms using intelligent AI agents, generates smart medical reports, performs risk analysis, and provides admin analytics dashboards.

Features

Authentication System
User Login & Registration
Admin Login
Forgot Password with Security Questions
Session Management
AI Diagnosis System

The project uses multiple AI agents for disease analysis:

❤️ Cardio AI → Heart-related analysis
🧠 Psycho AI → Mental health analysis
🫁 Pulmo AI → Lung & respiratory analysis
📄 Smart Medical Reports
AI-generated diagnosis
Risk level detection
Downloadable PDF reports
Structured healthcare report design

📊 Admin Dashboard
Total reports analytics
User management
Risk distribution charts
Disease statistics
Report management
🛠 Tech Stack
Technology	Purpose
Python	Backend Logic
Streamlit	Frontend UI
SQLite	Database
Pandas	Analytics
ReportLab	PDF Generation
HTML/CSS	Custom UI Styling

📁 Project Structure
medi_scan_ai/
│
├── agents/
│   ├── cardio.py
│   ├── psycho.py
│   └── pulmo.py
│
├── auth/
│   ├── login.py
│   └── register.py
│
├── utils/
│   └── preprocess.py
│
├── app.py
├── database.py
├── pdf_utils.py
├── landing.py
├── auth_ui.py
└── requirements.txt

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/medi-scan-ai.git
cd medi-scan-ai
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Application
streamlit run app.py

🔐 Default Admin Credentials
Username: admin
Password: admin123
📸 Modules
🏠 Landing Page

Modern healthcare-themed landing page with hover cards and AI highlights.

🔐 Authentication

Beautiful login/register UI with dark modern design.

🤖 AI Assistant

Analyze symptoms instantly with AI-generated insights.

📄 Generate Report

Create professional AI medical reports with PDF export.

📊 Admin Dashboard

Manage reports, users, and monitor analytics.

📈 Future Improvements
Real Machine Learning Models
OCR Medical Report Scanner
AI Chatbot Integration
Cloud Deployment
X-ray/Image Analysis
Email Report System
🧠 Project Flow
User Input
   ↓
Preprocessing
   ↓
AI Agents
   ↓
Risk Analysis
   ↓
PDF Report
   ↓
Database Storage
   ↓
Admin Dashboard Analytics
