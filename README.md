# 🌟 Astronomy AI Tutor: RAG-Based Chatbot

*Project 1 - ASTRON 1221: Astronomy Programming Course*

An intelligent AI tutor that helps students learn astronomy programming concepts by answering questions based on course lecture materials using Retrieval-Augmented Generation (RAG) technology.

## 🚀 Features

### 🧠 **Intelligent Question Answering**
- **Context-Aware Responses**: Finds relevant course material and generates accurate answers
- **Source Attribution**: Shows which lecture materials were used to generate each response
- **Natural Language Processing**: Understands questions in plain English

### 📚 **Comprehensive Knowledge Base** 
- **10 Lecture Files**: Processes all course materials automatically
- **137 Knowledge Chunks**: Semantic chunking by section headers for precise retrieval
- **Multi-Topic Coverage**: Python basics, NumPy, matplotlib, data analysis, Git, and more

### 💬 **Professional Chat Interface**
- **Streamlit Web App**: Clean, professional chat interface
- **Real-time Responses**: Fast AI-powered answers with loading indicators
- **Conversation History**: Maintains chat history throughout session
- **Sample Questions**: Pre-built questions to help users get started

### 🔒 **Secure & User-Friendly**
- **API Key Protection**: Secure password input for Anthropic API keys
- **Error Handling**: Robust error management with helpful messages
- **Performance Optimization**: Smart caching prevents reloading of embeddings

## � Live Demo

**🚀 Try it now!** The Astronomy AI Tutor is live and ready to use:

**👉 [https://astron-1221-ai-tutor.streamlit.app/](https://astron-1221-ai-tutor.streamlit.app/)**

Simply visit the link above to start chatting with the AI tutor instantly! No installation required - just enter your Anthropic API key and begin asking questions about astronomy programming.

## �🏗️ Architecture

### **RAG Pipeline**
```
User Question → Semantic Search → Context Retrieval → AI Generation → Response
```

### **Three-Class Design**
1. **`DocumentProcessor`**: Loads and chunks markdown lecture files
2. **`VectorStore`**: Creates embeddings and performs similarity search
3. **`AITutor`**: Orchestrates RAG pipeline with Anthropic Claude integration

### **Technology Stack**
- **Frontend**: Streamlit web framework
- **AI Model**: Anthropic Claude 4 Sonnet
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2)
- **Vector Search**: Cosine similarity with PyTorch tensors
- **Language**: Python 3.8+

## 📋 Prerequisites

- Python 3.8 or higher
- Anthropic API key ([Get one here](https://console.anthropic.com/))
- 2GB+ RAM (for loading sentence transformer models)
- Internet connection (for initial model downloads)

## ⚡ Quick Start

### 1. **Clone the Repository**
```bash
git clone https://github.com/JacobParzych/project1.git
cd project1
```

### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3. **Set Up Environment**
Create a `.env` file in the project root:
```env
ANTHROPIC_API_KEY=your-api-key-here
```

### 4. **Run the Application**
```bash
streamlit run app.py
```

### 5. **Start Chatting**
1. Open your browser to `http://localhost:8501`
2. Enter your Anthropic API key in the sidebar
3. Wait for initialization (first run takes ~30 seconds)
4. Ask questions about astronomy programming!

## 💡 Usage Examples

### **Sample Questions to Try:**
- "What is this course about?"
- "How do I use Python for astronomy?"
- "What is NumPy used for?"
- "How do I create plots with matplotlib?"
- "What are the main programming concepts covered?"
- "How do I work with variables in Python?"
- "What is object-oriented programming?"

### **Example Interaction:**
```
👤 Student: "How do I create a scatter plot?"

📚 Found relevant content from: Lecture6_Data_Visualization_20250910 (similarity: 0.847)

🤖 AI Tutor: To create a scatter plot in Python, you'll use matplotlib's pyplot module. Here's the basic pattern:

```python
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

# Create scatter plot
plt.scatter(x, y)
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label') 
plt.title('My Scatter Plot')
plt.show()
```

This is particularly useful in astronomy for plotting things like magnitude vs. color diagrams or position data from observations.
```

## 📁 Project Structure

```
project1/
├── astron1221_tutor.py          # Main Streamlit application
├── Project1_Parzych_Jamison.ipynb # Development notebook with analysis
├── requirements.txt             # Python dependencies
├── .env                        # Environment variables (create this)
├── README.md                   # This file
└── Lecture/                    # Course materials directory
    ├── Lecture1_Welcome_and_Setting_Up_20250826.md
    ├── Lecture2_Variables_and_Collections_20250828.md
    ├── Lecture3_Control_Flow_and_File_Operations_20250901.md
    ├── Lecture4_Numerical_Computing_20250903.md
    ├── Lecture5_Functions_and_Object-Oriented_Programming_20250909.md
    ├── Lecture6_Data_Visualization_20250910.md
    ├── Lecture7_LLM_API_Basics_20250913.md
    ├── Lecture8_LLM_Function_Tools_and_RAG_20250918.md
    ├── Lecture9_Github_20250920.md
    └── Lecture10_Streamlit_20250921.md
```

## 🔧 Configuration

### **API Settings**
- **Token Limit**: 500 tokens per response (~375 words)
- **Model**: Claude 4 Sonnet (fast, cost-effective)
- **Context**: Top 3 most relevant chunks per query
- **Similarity Threshold**: 0.1 minimum for relevance

### **Performance Settings**
- **Caching**: Embeddings cached per session
- **Chunk Size**: Variable (based on section headers)
- **Max Context**: 400 characters per chunk
- **Model Size**: 384-dimensional embeddings

## 🛠️ Development

### **Running the Jupyter Notebook**
For development and analysis:
```bash
jupyter notebook Project1_Parzych_Jamison.ipynb
```

### **Key Development Features:**
- **Data Analysis**: Visualizations of chunk distribution and statistics
- **Testing Suite**: Comprehensive error handling tests
- **Performance Monitoring**: Embedding creation and search timing
- **Debug Tools**: Built-in debugging panel in Streamlit app

### **Adding New Lecture Materials**
1. Place `.md` files in the `Lecture/` directory
2. Ensure files use `## ` for section headers
3. Restart the application to reprocess

## 📊 Performance Metrics

- **Initial Load Time**: ~30-45 seconds (first run)
- **Subsequent Loads**: ~2-3 seconds (cached)
- **Query Response Time**: ~1-2 seconds
- **Memory Usage**: ~500MB (with loaded models)
- **Knowledge Base**: 137 chunks from 10 lectures

## 🚨 Troubleshooting

### **Common Issues:**

**"Import errors" in development environment:**
- This is normal - packages work fine when running with Streamlit
- Install missing packages: `pip install -r requirements.txt`

**"API key not working":**
- Verify key is correct in `.env` file
- Check Anthropic account has available credits
- Ensure no extra spaces in the key

**"App won't load new questions":**
- Refresh the browser page
- Check browser console for JavaScript errors
- Use the "Clear Chat History" button in debug panel

**"Slow response times":**
- First run is always slower (model downloads)
- Check internet connection for API calls
- Restart app if memory usage is high

## 🎓 Educational Objectives

This project demonstrates proficiency in:

### **Programming Concepts**
- **Object-Oriented Programming**: Clean class design with clear responsibilities
- **File I/O Operations**: Reading and processing multiple file formats
- **Error Handling**: Comprehensive try/except blocks and user feedback
- **Data Structures**: Efficient use of lists, dictionaries, and NumPy arrays

### **Modern AI Integration**
- **API Integration**: Secure handling of external AI services
- **Embedding Technologies**: Semantic search with sentence transformers
- **RAG Architecture**: Retrieval-augmented generation implementation
- **Web Development**: Professional interface with Streamlit

### **Software Engineering**
- **Code Organization**: Modular design with clear separation of concerns
- **Performance Optimization**: Caching and efficient data processing
- **User Experience**: Intuitive interface with helpful feedback
- **Documentation**: Comprehensive code comments and README

## 📈 Future Enhancements

### **Planned Features**
- **Multi-format Support**: PDF, HTML, and Word document processing
- **Advanced Chunking**: Intelligent text splitting based on content type
- **Conversation Memory**: Long-term chat history across sessions
- **Export Features**: Save conversations and generate study guides

### **Technical Improvements**
- **Vector Database**: Migration to Pinecone or Weaviate for scalability
- **Fine-tuned Embeddings**: Custom embeddings trained on astronomy content
- **Multi-model Support**: Integration with GPT-4, Gemini, and other LLMs
- **Real-time Updates**: Live reloading when lecture materials change

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes** with clear commit messages
4. **Add tests** for new functionality
5. **Submit a pull request** with a detailed description

### **Development Guidelines**
- Follow PEP 8 style guidelines
- Add docstrings to all functions and classes  
- Include error handling for edge cases
- Update README for new features

## 📜 License

This project is developed for educational purposes as part of ASTRON 1221. Please respect course policies regarding code sharing and collaboration.

## 👥 Authors

- **Jacob Parzych** - 
- **Niko Jamison** - 

## 🙏 Acknowledgments

- **ASTRON 1221 Course Staff** - For providing comprehensive lecture materials
- **Anthropic** - For Claude AI API access
- **Sentence Transformers Team** - For open-source embedding models
- **Streamlit** - For the excellent web framework

## 📞 Support

Having issues? Here's how to get help:

1. **Check the Troubleshooting section** above
2. **Review the Issues tab** on GitHub
3. **Create a new issue** with detailed error messages
4. **Contact course staff** for academic questions

---

**Happy Learning! 🌟**

*Transform your astronomy programming knowledge with AI-powered assistance.*