from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import torch
import spacy

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
tokenizer = AutoTokenizer.from_pretrained('/mnt/shareddrive/Research/Thesis/Thesis/save_models/pico-ner')
model = AutoModelForTokenClassification.from_pretrained('/mnt/shareddrive/Research/Thesis/Thesis/save_models/pico-ner')
nlp = pipeline("ner", model=model, tokenizer=tokenizer,device=device)

def get_pico(doc_list):

    return [nlp(doc) for doc in doc_list.keys()]

def format_result(result_list):
    pass
