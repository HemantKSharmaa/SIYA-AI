# SIYA AI 🤖

**SIYA** (Smart Intelligent Youth Assistant) is a Python-based AI voice assistant with a custom graphical user interface. It listens to your voice, understands your intent, and responds — whether that means answering a question, searching the web in real time, automating a task, or generating an image.

---

## ✨ Features

- 🎙️ **Voice Input** — Speak naturally; SIYA transcribes your voice using speech recognition
- 🔊 **Text-to-Speech Output** — Responses are spoken back to you in real time
- 🧠 **Smart Decision Layer** — A first-layer model routes your query to the right handler: chatbot, real-time search, or automation
- 🌐 **Real-Time Web Search** — Fetches live answers for time-sensitive queries
- ⚙️ **Task Automation** — Open/close apps, play media, perform Google or YouTube searches, and more
- 🎨 **Image Generation** — Generate AI images from natural language prompts
- 🖥️ **Custom GUI** — A built-in graphical interface with live chat display and assistant status
- 💾 **Chat Memory** — Conversation history is persisted via a JSON chat log

---

## 📁 Project Structure

```
SIYA-AI/
│
├── Backend/
│   ├── Chatbot.py           # Handles general conversational queries
│   ├── RealtimeSearchEngine.py  # Performs real-time web searches
│   ├── SpeechToText.py      # Converts microphone input to text
│   ├── TextToSpeech.py      # Converts text responses to audio
│   ├── Automation.py        # Handles system/task automation commands
│   ├── ImageGeneration.py   # AI image generation module
│   └── Model.py             # First-layer decision-making model (DMM)
│
├── Frontend/
│   └── GUI.py               # Graphical user interface
│
├── Data/
│   └── ChatLog.json         # Persistent conversation history
│
├── Main.py                  # Entry point — ties all modules together
├── Requirements.txt         # Python dependencies
└── .env                     # Environment variables (username, assistant name, API keys)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- A microphone
- API keys (configured in `.env`)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/HemantKSharmaa/SIYA-AI.git
   cd SIYA-AI
   ```

2. **Install dependencies**
   ```bash
   pip install -r Requirements.txt
   ```

3. **Set up your `.env` file**

   Open the `.env` file and fill in your details:
   ```env
   Username=YourName
   Assistantname=SIYA
   # Add any required API keys here
   ```

4. **Run SIYA**
   ```bash
   python Main.py
   ```

---

## 🛠️ How It Works

1. SIYA listens for your voice via the microphone.
2. Your speech is converted to text using the `SpeechToText` module.
3. The **First Layer Decision Model** classifies the query as:
   - `general` → handled by the AI Chatbot
   - `realtime` → handled by the Real-Time Search Engine
   - `open / close / play / system / ...` → handled by the Automation module
   - `generate` → triggers the Image Generation pipeline
4. The response is displayed in the GUI and spoken aloud via Text-to-Speech.

---

## 📺 Demo

Watch SIYA in action: [YouTube Demo](https://youtu.be/E4fGvJ2nGkY?si=mE3yeL3eNry_ufDs)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a pull request or raise an issue.

---

## 📄 License

This project is open source. See the [LICENSE](LICENSE) file for details.

---

> Built with ❤️ by [Hemant Kumar Sharma](https://github.com/HemantKSharmaa)
