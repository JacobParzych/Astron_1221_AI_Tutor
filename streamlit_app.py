import streamlit as st
import os
import glob
import numpy as np
from sentence_transformers import SentenceTransformer
import anthropic
from typing import List, Dict
from dotenv import load_dotenv
import warnings


# Load environment variables
load_dotenv()
warnings.filterwarnings('ignore')

# Set page configuration
st.set_page_config(
    page_title="Astronomy AI Tutor Chat",
    page_icon="🌟",
    layout="wide"
)

class DocumentProcessor:
    """
    A simplified class to process lecture documents for RAG implementation.
    """
    
    def __init__(self, lecture_directory: str):
        """Initialize the DocumentProcessor."""
        self.lecture_directory = lecture_directory
        self.chunks = []
        
    def load_and_process_documents(self) -> None:
        """Load all markdown files and process them into chunks."""
        try:
            # Find all markdown files
            pattern = os.path.join(self.lecture_directory, "*.md")
            markdown_files = glob.glob(pattern)
            
            if not markdown_files:
                raise FileNotFoundError(f"No markdown files found in {self.lecture_directory}")
            
            st.info(f"📚 Found {len(markdown_files)} lecture files")
            
            total_chunks = 0
            for file_path in markdown_files:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                filename = os.path.basename(file_path).replace('.md', '')
                doc_chunks = self.chunk_by_sections(content, filename)
                self.chunks.extend(doc_chunks)
                total_chunks += len(doc_chunks)
            
            st.success(f"✅ Processed {total_chunks} chunks from lecture materials")
                    
        except Exception as e:
            st.error(f"Error processing documents: {e}")
            raise
    
    def chunk_by_sections(self, text: str, source_filename: str) -> List[Dict]:
        """Split document into chunks based on ## section headers."""
        sections = text.split('\n## ')
        chunks = []
        
        for i, section in enumerate(sections):
            # Add back the '## ' that was removed during split
            if i == 0:
                chunk_text = section
            else:
                chunk_text = '## ' + section
            
            # Only keep chunks with substantial content
            if len(chunk_text.strip()) > 100:
                chunks.append({
                    'text': chunk_text.strip(),
                    'source_file': source_filename,
                    'chunk_id': i
                })
        
        return chunks
    
    def get_chunks(self) -> List[Dict]:
        """Return the processed chunks."""
        return self.chunks

class VectorStore:
    """
    A simplified class to manage embeddings and similarity search.
    """
    
    def __init__(self):
        """Initialize the VectorStore."""
        with st.spinner("🔄 Loading sentence transformer model..."):
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.chunks = []
        self.embeddings = None
        
    def add_chunks(self, chunks: List[Dict]) -> None:
        """Add chunks and create embeddings."""
        with st.spinner(f"🧠 Creating embeddings for {len(chunks)} chunks..."):
            self.chunks = chunks
            chunk_texts = [chunk['text'] for chunk in chunks]
            self.embeddings = self.model.encode(chunk_texts, convert_to_tensor=True)
        
        st.success(f"✅ Created embeddings with dimension: {self.embeddings.shape[1]}")
    
    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        """Search for relevant chunks based on similarity."""
        if self.embeddings is None:
            return []
        
        # Get query embedding
        query_embedding = self.model.encode([query], convert_to_tensor=True)
        
        # Calculate similarities
        from sentence_transformers.util import cos_sim
        similarities = cos_sim(query_embedding, self.embeddings)[0]
        
        # Get top results
        top_indices = similarities.argsort(descending=True)[:top_k]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # minimum similarity threshold
                result = self.chunks[idx].copy()
                result['similarity_score'] = float(similarities[idx])
                results.append(result)
        
        return results

class AITutor:
    """
    A simple RAG-based AI tutor using Anthropic's Claude.
    """
    
    def __init__(self, lecture_directory: str, api_key: str = None):
        """Initialize the AI Tutor."""
        self.document_processor = DocumentProcessor(lecture_directory)
        self.vector_store = VectorStore()
        
        # Setup Anthropic client
        if api_key:
            try:
                self.client = anthropic.Anthropic(api_key=api_key)
                st.success("✅ Anthropic API key connected successfully")
            except Exception as e:
                st.error(f"❌ Anthropic API setup failed: {e}")
                self.client = None
        else:
            self.client = None
    
    def initialize(self):
        """Load documents and create embeddings."""
        with st.spinner("🚀 Initializing AI Tutor..."):
            # Process documents
            self.document_processor.load_and_process_documents()
            chunks = self.document_processor.get_chunks()
            
            # Create embeddings
            self.vector_store.add_chunks(chunks)
        
        st.success("🎉 AI Tutor Ready!")
    
    def ask(self, question: str) -> str:
        """Ask a question and get an AI response."""
        # Find relevant content using top 3 chunks
        relevant_chunks = self.vector_store.search(question, top_k=3)
        
        if not relevant_chunks:
            return "Sorry, I couldn't find relevant information for your question in the course materials."
        
        if not self.client:
            return "AI responses not available. Please enter your Anthropic API key in the sidebar."
        
        # Prepare context from retrieved chunks
        context = "\n\n".join([chunk['text'][:400] for chunk in relevant_chunks])
        
        # Simple prompt for Claude
        prompt = f"""Answer this student's question about astronomy programming based on the course materials:

Question: {question}

Course Materials:
{context}

Provide a clear, helpful answer as an astronomy programming tutor."""
        
        try:
            response = self.client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=300,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error getting AI response: {e}"

# Cache the tutor initialization to prevent reloading
@st.cache_resource
def initialize_tutor(api_key):
    """Initialize the AI tutor with caching."""
    tutor = AITutor("Lecture", api_key)
    tutor.initialize()
    return tutor

# Main Streamlit App
def main():
    st.title("🌟 Astronomy AI Tutor Chatbot")
    st.markdown("Ask me anything about the astronomy programming course materials!")
    
    # Sidebar for API key
    with st.sidebar:
        st.header("⚙️ Configuration")
        api_key = st.text_input(
            "Anthropic API Key:", 
            type="password",
            help="Enter your Claude API key to enable AI responses"
        )
        
        if api_key:
            st.success("🔑 API Key provided")
        else:
            st.warning("⚠️ Enter API key for AI responses")
        
        st.markdown("---")
        st.markdown("### About")
        st.info("This chatbot uses RAG (Retrieval-Augmented Generation) to answer questions about astronomy programming course materials.")
        
        # Show sample questions
        st.markdown("### 💡 Try asking:")
        sample_questions = [
            "What is this course about?",
            "How do I use Python for astronomy?",
            "What is NumPy used for?",
            "How do I create plots with matplotlib?",
            "What are the main programming concepts covered?"
        ]
        for q in sample_questions:
            if st.button(q, key=f"sample_{q[:20]}"):
                st.session_state.sample_question = q
    
    # Initialize the tutor
    if api_key:
        try:
            tutor = initialize_tutor(api_key)
        except Exception as e:
            st.error(f"Failed to initialize tutor: {e}")
            return
    else:
        st.info("👈 Please enter your Anthropic API key in the sidebar to begin chatting")
        return
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm your astronomy programming tutor. I can help you with questions about Python, NumPy, matplotlib, data analysis, and all the topics covered in the course materials. What would you like to learn about?"}
        ]
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Handle sample question from sidebar
    if "sample_question" in st.session_state:
        prompt = st.session_state.sample_question
        del st.session_state.sample_question
    else:
        prompt = None
    
    # Chat input
    if prompt or (prompt := st.chat_input("Ask me about astronomy programming...")):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("🤔 Thinking..."):
                response = tutor.ask(prompt)
            st.write(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()