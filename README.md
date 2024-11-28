# Genio
A website that dynamically generates content based on user input using Gemini.

### README for AI-Powered Website Generator

---

#### **Project Overview**
This project is a Python-based web application that generates a webpage about a given topic. The page includes:
- A brief description of the topic generated using the **Google Gemini AI API**.
- Images sourced via Google Images.
- An embedded YouTube video related to the topic.

The app is built using **Flask** and requires several external libraries for functionality.

---

#### **Prerequisites**
1. **Python** (Version 3.8 or higher)
2. API Key for **Google Gemini** (Generative AI)
3. Required Python libraries:
   - `google-generativeai`
   - `flask`
   - `urllib`
   - `requests`
   - `beautifulsoup4`
4. Basic knowledge of using terminal/command line.

---

#### **Installation Steps**

1. **Clone or Download the Repository**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate    # For Linux/Mac
   venv\Scripts\activate       # For Windows
   ```

3. **Install Required Libraries**
   Run the following command to install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Your Google Gemini API Key**
   - Locate the line in `app.py`:
     ```python
     api_key1 = "Enter-API-Key"
     ```
   - Replace `"Enter-API-Key"` with your API key for **Google Gemini**.

---

#### **Running the Application**
1. Start the server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

### **Video previrew** 

https://github.com/user-attachments/assets/f8e9abf7-fac5-4e9e-89a7-2389448fe54b

#### **Future Enhancements**
- Add user authentication.
- Enable database storage for history and analytics.
- Enhance error handling and logging.

---

#### **Contact**
For support or feedback, contact karam.hwete@gmail.com.
