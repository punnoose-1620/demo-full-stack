# AI-Powered Web Application Framework

A full-stack web application that demonstrates an AI-powered framework similar to Lovable.ai, built as an assessment task for an AI firm. This application leverages Claude and Gemini AI models to generate intelligent responses and interactive HTML content.

## 🚀 Project Overview

This application creates a framework where users can input their requirements, and the backend intelligently processes these inputs using AI models (Claude and Gemini) to generate responses. The system automatically detects HTML content in the responses and presents it as clickable buttons, allowing users to view the generated HTML pages in new tabs.

### Key Features

- **AI-Powered Response Generation**: Uses Claude 3.5 Sonnet and Gemini 1.5 Flash models
- **Smart HTML Detection**: Automatically identifies HTML content in AI responses
- **Interactive UI**: Displays HTML content as clickable "View Page" buttons
- **Fallback System**: Graceful error handling with model fallback
- **Modern UI**: Clean, responsive design inspired by Lovable.ai

## 🛠️ Technical Architecture

### Backend (Flask)
- **Framework**: Flask 3.0.2
- **AI Integration**: 
  - Anthropic Claude API (primary)
  - Google Gemini API (fallback)
- **Error Handling**: Comprehensive error management for network and API issues

### Frontend
- **HTML/CSS/JavaScript**: Modern responsive design
- **HTML Content Processing**: JavaScript-based HTML extraction and rendering
- **Dynamic UI**: Real-time response display with interactive elements

## 📁 Project Structure

```
demo-full-stack/
├── app.py                 # Main Flask application
├── controllers.py         # AI integration and response handling
├── Keys.py               # API key configuration (not included)
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css     # Application styling
│   └── images/
│       └── favicon.ico   # Site favicon
├── templates/
│   ├── index.html        # Main landing page
│   └── response.html     # Response display page
└── README.md            # This file
```

## 🔧 Setup and Installation

### Prerequisites
- Python 3.7+
- API keys for Claude and Gemini

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd demo-full-stack
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API keys**
   Create a `Keys.py` file with your API keys:
   ```python
   CLAUDE_SONET_API = "your-claude-api-key"
   GEMINI_API = "your-gemini-api-key"
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:8000`

## 🎯 How It Works

### 1. User Input Processing
- Users enter their requirements in the web interface
- The input is sent to the backend via Flask routes

### 2. AI Response Generation
- The backend first attempts to get a response from Claude 3.5 Sonnet
- If Claude fails, it automatically falls back to Gemini 1.5 Flash
- Hidden prompts are injected to guide the AI to generate HTML content

### 3. Response Processing
- The AI response is analyzed for HTML content
- HTML code blocks are extracted and converted to clickable buttons
- Non-HTML content is displayed as regular text

### 4. User Interface
- HTML content appears as "View Page" buttons
- Clicking a button opens the generated HTML in a new tab
- Regular text content is displayed inline

## 🔄 API Integration

### Claude Integration
- **Model**: `claude-3-5-sonnet-20241022`
- **Max Tokens**: 1024
- **Error Handling**: Connection, timeout, and API errors

### Gemini Integration
- **Model**: `gemini-1.5-flash-002`
- **Fallback**: Used when Claude is unavailable
- **Error Handling**: Permission and authentication errors

## 🎨 UI/UX Features

- **Modern Design**: Clean, professional interface
- **Responsive Layout**: Works on desktop and mobile devices
- **Interactive Elements**: Hover effects and smooth transitions
- **Chat Interface**: Sidebar with conversation history
- **Real-time Updates**: Dynamic content loading

## 🚨 Error Handling

The application includes comprehensive error handling for:
- Network connectivity issues
- API authentication failures
- Timeout errors
- Permission denied errors
- Unauthenticated access

## 🔒 Security Considerations

- API keys are stored in a separate `Keys.py` file (not included in repository)
- Input validation and sanitization
- Error messages don't expose sensitive information

## 📝 Usage Examples

1. **Generate a simple HTML page**: "Create a contact form with modern styling"
2. **Build interactive components**: "Make a calculator with JavaScript"
3. **Design landing pages**: "Create a product landing page for a tech startup"

## 🤝 Contributing

This project was created as an assessment task. For any improvements or suggestions, please feel free to submit issues or pull requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built as an assessment task for an AI firm
- Inspired by Lovable.ai's customer engagement platform
- Uses Claude and Gemini AI models for intelligent response generation
