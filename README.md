# 🧠 AI Code Refactoring API (Django)

This project provides a REST API to refactor source code using a locally hosted transformer model (e.g., fine-tuned CodeT5). It supports input via JSON and returns a refactored version of the code.

---

## 🚀 Project Structure

code_refactor_api/
├── refactor_project/
│ ├── settings.py
│ ├── urls.py
│ ├── model_runner.py # Core model logic
│ └── refactoring_model/ # Contains tokenizer and model files (ignored from Git)
├── api/
│ ├── views.py # API logic
│ └── urls.py
├── manage.py
├── .gitignore
└── README.md


---

## ✅ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/IT21440236/refactoring-api.git
cd refactoring-api

2. Create a virtual environment & activate it

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3.Install dependencies
pip install -r requirements.txt

If requirements.txt is missing, run:
pip install django djangorestframework transformers torch

4.Start the server
python manage.py runserver

The API will be available at:
http://127.0.0.1:8000/api/refactor/


🧪 Test the Endpoint (cURL)
curl --location 'http://127.0.0.1:8000/api/refactor/' \
--header 'Content-Type: application/json' \
--data '{
    "code": "public class PriceCalculator {\n\n    public static double calculateDiscount(double price, String discount) {\n        if (discount.equals(\"None\")) {\n            return price;\n        } else if (discount.equals(\"Silver\")) {\n            return price - (price * 0.05);\n        } else if (discount.equals(\"Gold\")) {\n            return price - (price * 0.1);\n        } else if (discount.equals(\"Platinum\")) {\n            return price - (price * 0.2);\n        } else {\n            return price;\n        }\n    }\n}"
}'

📓 Colab Notebook
Use the Colab notebook to fine-tune or interactively test the model:
🔗 [Open in Colab](https://drive.google.com/file/d/1Ay_oj0DfK73saXzNKP2DctvHByUUtpal/view)

🧠 Model
The model used is a transformer-based sequence-to-sequence model trained/fine-tuned for code refactoring. It is loaded from the local refactor_project/refactoring_model/ directory and includes:

tokenizer.json

model.safetensors

config.json

generation_config.json
