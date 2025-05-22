import streamlit as st
import os
from datetime import date
from src.langgraphagenticai.ui.streamlitui.uiconfigfile import Config
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_control = {}