

## ** Description**
This calculator performs **addition, subtraction, multiplication, and division**. It includes a built-in **history feature**, allowing users to:
✅ **Store past calculations**  
✅ **Retrieve calculation history**  
✅ **Recall the last calculation**  
✅ **Clear calculation history**  

For **division by zero**, the function **returns an "ERROR: Division by zero" message** instead of raising an exception.

I implemented this using a combination of **static, class, and instance methods** for efficient handling of calculations and history.

To ensure accuracy and reliability, the calculator is **thoroughly tested** using:
- ✅ **Pytest** (unit testing)
- ✅ **Pylint** (code quality/linting)
- ✅ **Coverage (cov)** (test coverage measurement)

---

## **📌 Setup & Installation**
### **Step 1️⃣: Clone the Repository**
```bash
git clone https://github.com/jfm56/calculator.git
cd calculator
```

### **Step 2️⃣: Create a Virtual Environment**
```bash
python -m venv venv
```

### **Step 3️⃣: Activate the Virtual Environment**
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```
- **Windows (Command Prompt):**
  ```bash
  venv\Scripts\activate
  ```
- **Windows (PowerShell):**
  ```powershell
  venv\Scripts\Activate.ps1
  ```

### **Step 4️⃣: Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## **📌 Running Tests**
To ensure the calculator functions correctly, run:
```bash
pytest --pylint --cov
```

- ✅ **Pytest** runs unit tests.
- ✅ **Pylint** checks for code style issues.
- ✅ **Coverage (cov)** measures test coverage.
