import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os

model_path = os.path.join(os.path.dirname(__file__), "refactoring_model")
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def run_refactor_model(code: str, generation_config=None) -> str:
    if not generation_config:
        generation_config = {
            "num_beams": 5,
            "max_length": 512,
            "temperature": 1.0,
            "top_k": 50,
            "top_p": 0.95
        }

    inputs = tokenizer(code, return_tensors="pt", max_length=generation_config["max_length"],
                       truncation=True, padding="max_length").to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=generation_config["max_length"],
            num_beams=generation_config["num_beams"],
            temperature=generation_config["temperature"],
            top_k=generation_config["top_k"],
            top_p=generation_config["top_p"],
            early_stopping=True
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
