# Constitution Chatbot

<img src="project-images/anayasa_chatbot.png" alt="Anayasa Chatbot Banner" width="850" height="500">  <!-- Add an image relevant to your project -->

## 📑 About the Project

Constitution Chatbot is an artificial intelligence-based question-answer system trained on the Constitution of the Republic of Turkey. This project was developed so that citizens can easily learn their constitutional rights and state structure. Using a dataset of 875 questions and answers created with the Gemini-1.5 Flash model, the Llama-3.8 model was fine-tuned and made available to everyone with a comprehensive Django web application.

## 🌟 Features

- **Constitution Expert Chatbot**: Customized AI model that can answer your questions about the Constitution of the Republic of Turkey
- **User Account System**: Registration and login system for secure access
- **Conversation History**: Ability to view users' previous chats
- **Responsive Design**: Interface usable on all screen sizes, including mobile devices
- **Fast and Accurate Answers**: Optimized performance with finetuned version of Llama-3.8 model


## 🔧 Technologies

### Model Training
- **Data Collection and Processing**: PyPDF2, Pandas, CSV
- **Model Training**:
- Gemini-1.5 Flash (dataset creation)
- Llama-3.8 (fine-tuning)
- Unsloth (optimization)
- PyTorch

### Web Application
- **Backend**: Django
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Database**: SQLite/PostgreSQL
- **Deployment**: Hugging Face Model Hosting

## 🚀 Installation

### Requirements
- Python 3.8+
- Django 4.0+
- PyTorch
- Unsloth
- Hugging Face Transformers

## 📊 Dataset Creation Process

The dataset used in this project includes 875 question-answer pairs extracted from the Constitution of the Republic of Turkey. Dataset creation process:

1. Constitution text extracted from PDF
2. Question-answer pairs created using Gemini-1.5 Flash model
3. Data cleaning and normalization processes applied
4. Prepared for fine-tuning to Llama-3.8 model

Some topics covered in the dataset:
- Fundamental rights and freedoms
- Legislative, executive and judicial
- Constitutional amendments
- Citizenship rights
- State structure

## 👥 User Interface

The web application includes the following pages:
- **Homepage**: Project introduction and features
- **Chatbot Page**: Area for interaction with AI
- **About Me**: Project and developer information
- **Register/Login**: User account management
- **Conversation History**: View previous chats
- **Conversation History**: View conversation details

## 🖼️ Project Screenshots

### 🏠 Homepage
![Homepage](project-images/home.png)

### 🏠 Chatbot Page
![Chatbot Page](project-images/chatbot.png)

### 🏠 About Me
![About Me](project-images/about.png)

### 🏠 Conversation History
![Conversation History](project-images/chat-history.png)

### 🏠 Conversation Detail
![Conversation Detail](project-images/chat-detail.png)

<svg viewBox="0 0 900 600" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="900" height="600" fill="#f8f9fa" rx="10" ry="10"/>
  
  <!-- Title -->
  <text x="450" y="50" font-family="Arial, sans-serif" font-size="24" font-weight="bold" text-anchor="middle" fill="#333">AnayasAI Model Mimarisi</text>
  
  <!-- Data Collection Stage -->
  <rect x="50" y="100" width="200" height="120" rx="10" ry="10" fill="#e3f2fd" stroke="#2196f3" stroke-width="2"/>
  <text x="150" y="130" font-family="Arial, sans-serif" font-size="18" font-weight="bold" text-anchor="middle" fill="#0d47a1">Veri Toplama &amp; İşleme</text>
  <text x="150" y="160" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- Anayasa PDF Çıkarımı</text>
  <text x="150" y="180" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- Gemini-1.5 Flash</text>
  <text x="150" y="200" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- 875 Soru-Cevap Çifti</text>
  
  <!-- Model Training Stage -->
  <rect x="350" y="100" width="200" height="120" rx="10" ry="10" fill="#e8f5e9" stroke="#4caf50" stroke-width="2"/>
  <text x="450" y="130" font-family="Arial, sans-serif" font-size="18" font-weight="bold" text-anchor="middle" fill="#1b5e20">Model Eğitimi</text>
  <text x="450" y="160" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- Llama-3.8 Base</text>
  <text x="450" y="180" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- Unsloth Optimizasyon</text>
  <text x="450" y="200" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- PyTorch Fine-Tuning</text>
  
  <!-- Deployment Stage -->
  <rect x="650" y="100" width="200" height="120" rx="10" ry="10" fill="#fff3e0" stroke="#ff9800" stroke-width="2"/>
  <text x="750" y="130" font-family="Arial, sans-serif" font-size="18" font-weight="bold" text-anchor="middle" fill="#e65100">Model Dağıtımı</text>
  <text x="750" y="160" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- Hugging Face</text>
  <text x="750" y="180" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- Django Entegrasyonu</text>
  <text x="750" y="200" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- Web Dağıtımı</text>
  
  <!-- Arrows between stages -->
  <line x1="250" y1="160" x2="350" y2="160" stroke="#666" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="550" y1="160" x2="650" y2="160" stroke="#666" stroke-width="2" marker-end="url(#arrowhead)"/>
  
  <!-- Model Architecture Details -->
  <rect x="200" y="280" width="500" height="230" rx="10" ry="10" fill="#f3e5f5" stroke="#9c27b0" stroke-width="2"/>
  <text x="450" y="310" font-family="Arial, sans-serif" font-size="18" font-weight="bold" text-anchor="middle" fill="#4a148c">Llama-3.8 Model Detayları</text>
  
  <!-- Model Parameters Box -->
  <rect x="220" y="330" width="220" height="160" rx="5" ry="5" fill="#f9fbe7" stroke="#cddc39" stroke-width="1"/>
  <text x="330" y="350" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#827717">Model Parametreleri</text>
  <text x="330" y="380" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- max_seq_length: 2048</text>
  <text x="330" y="400" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- load_in_4bit: True</text>
  <text x="330" y="420" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- Optimizer: adamw_8bit</text>
  <text x="330" y="440" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- Learning Rate: 2e-4</text>
  <text x="330" y="460" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- weight_decay=0.01</text>
  <text x="330" y="480" font-family="Arial, sans-serif" font-size="14" text-anchor="middle" fill="#333">- max_steps=120</text>
  
  <!-- Web Application -->
  <rect x="50" y="530" width="800" height="50" rx="10" ry="10" fill="#ffebee" stroke="#f44336" stroke-width="2"/>
  <text x="450" y="560" font-family="Arial, sans-serif" font-size="18" font-weight="bold" text-anchor="middle" fill="#b71c1c">Django Web Uygulaması (Frontend: HTML5, CSS3, Bootstrap 5, JavaScript)</text>
  
  <!-- Arrow markers definition -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#666"/>
    </marker>
  </defs>
</svg>
## 🤖 Using the Model

You can use the trained model directly from Hugging Face:

```python
max_seq_length = 2048
dtype = None
load_in_4bit = True

if True:
    from unsloth import FastLanguageModel
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name="HasanCan6241/anayasa-lora-Llama-3.8",
        load_in_4bit=load_in_4bit,
        dtype=dtype,
        max_seq_length=max_seq_length,
    )
    FastLanguageModel.for_inference(model)

messages = [
    {"role": "user", "content": "Anayasaya göre en temel hak ve hürriyetlerim nelerdir?"}
]

input_ids = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to("cuda")

from transformers import TextStreamer
text_streamer = TextStreamer(tokenizer, skip_prompt=True)

outputs = model.generate(
    input_ids,
    streamer=text_streamer,
    max_new_tokens=256,
    pad_token_id=tokenizer.eos_token_id
)
```
Click here to access the [model](https://huggingface.co/HasanCan6241/anayasa-lora-Llama-3.8)

### Adımlar

1. Repoyu klonlayın:
```bash
git clone https://github.com/HasanCan6241/ConstituAI.git
cd anayasa-chatbot
```

2. Virtual environment oluşturun ve aktif edin:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. Veritabanı migrasyonlarını yapın:
```bash
python manage.py migrate
```

5. Projeyi çalıştırın:
```bash
python manage.py runserver
```

6. You can start using the application by going to `http://localhost:8000` in your browser.

## 📝 Lisans

This project is licensed under the [MIT License](LICENSE).
---

⭐ If you like this project, don't forget to star it!
