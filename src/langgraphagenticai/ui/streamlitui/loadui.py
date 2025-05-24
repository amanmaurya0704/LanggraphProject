import streamlit as st
import os
from datetime import date
from src.langgraphagenticai.ui.streamlitui.uiconfigfile import Config
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_control = {}
    
    def initialize_session(self):
        return {
        "current_step": "requirements",
        "requirements": "",
        "user_stories": "",
        "po_feedback": "",
        "generated_code": "",
        "review_feedback": "",
        "decision": None
    }
  


    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False
        
        

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_control["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_control["selected_llm"] == 'Groq':
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_control["selected_groq_model"] = st.selectbox("Select Model", model_options)
                # API key input
                self.user_control["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key",
                                                                                                      type="password")
                # Validate API key
                if not self.user_control["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
            
            elif self.user_control["selected_llm"] == 'Gemini':
                # Model selection
                model_options = self.config.get_gemini_model_options()
                
                self.user_control["selected_gemini_model"] = st.selectbox("Select Model", model_options)
                # API key input
                self.user_control["GEMINI_API_KEY"] = st.session_state["GEMINI_API_KEY"] = st.text_input("API Key",
                                                                                                      type="password")
                # Validate API key
                if not self.user_control["GEMINI_API_KEY"]:
                    st.warning("⚠️ Please enter your Gemini API key to proceed. Don't have? refer : https://console.cloud.google.com/apis/credentials")
                   
            
            # Use case selection
            self.user_control["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if self.user_control["selected_usecase"] =="Chatbot with Tool":
                # API key input
                os.environ["TAVILY_API_KEY"] = self.user_control["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY API KEY",
                                                                                                      type="password")
                # Validate API key
                if not self.user_control["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your TAVILY_API_KEY key to proceed. Don't have? refer : https://app.tavily.com/home")
            
            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()
            
            
        
        return self.user_control