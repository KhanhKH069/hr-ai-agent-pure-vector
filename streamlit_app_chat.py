#!/usr/bin/env python3
"""
HR AI Agent - ENHANCED VERSION
With Debug Mode, Chat History, Export & Professional UI
"""

import streamlit as st
import os
import sys
from datetime import datetime
from dotenv import load_dotenv

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
load_dotenv()

# Page config
st.set_page_config(
    page_title="HR AI Agent",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .debug-info {
        background-color: #f0f2f6;
        padding: 0.5rem;
        border-radius: 0.3rem;
        font-size: 0.85rem;
        margin-top: 0.5rem;
    }
    .stats-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 0.5rem;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HELPER FUNCTIONS
# ============================================

def validate_match(user_question, matched_question, distance):
    """Validate if match is good (prevents wrong answers)"""
    if distance < 0.5:
        return True
    
    user_words = set(user_question.lower().split())
    matched_words = set(matched_question.lower().split())
    
    stop_words = {'là', 'có', 'được', 'không', 'gì', 'như', 'thế', 'nào', 'bao', 'nhiêu',
                  'the', 'is', 'are', 'what', 'how', 'when', 'where', 'của', 'về'}
    user_words -= stop_words
    matched_words -= stop_words
    
    common = user_words & matched_words
    
    if distance < 0.6:
        return len(common) >= 1
    else:
        return len(common) >= 2

def query_vector_db(question):
    """Query ChromaDB with validation"""
    try:
        from services.vector_db import get_vector_db
        
        vdb = get_vector_db()
        results = vdb.query(
            collection_name='hr_policies',
            query_text=question,
            n_results=3
        )
        
        if results and results['documents'] and len(results['documents'][0]) > 0:
            for i in range(len(results['documents'][0])):
                metadata = results['metadatas'][0][i]
                distance = results['distances'][0][i] if 'distances' in results else 1.0
                
                if distance >= 0.7:
                    continue
                
                matched_q = metadata.get('question', '')
                if not validate_match(question, matched_q, distance):
                    continue
                
                similarity = round((1 - distance) * 100, 1)
                
                return {
                    'found': True,
                    'answer': metadata.get('answer', ''),
                    'question': matched_q,
                    'source': metadata.get('source_file', 'Unknown'),
                    'similarity': similarity,
                    'distance': distance,
                    'type': metadata.get('type', 'main')
                }
        
        return {'found': False}
        
    except Exception as e:
        return {'found': False, 'error': str(e)}

def export_chat_history():
    """Export chat as markdown"""
    if 'messages' not in st.session_state or len(st.session_state.messages) <= 1:
        return None
    
    export = f"# HR AI Chat Export\n\n"
    export += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    export += "---\n\n"
    
    for msg in st.session_state.messages[1:]:  # Skip welcome message
        role = "👤 User" if msg['role'] == 'user' else "🤖 Assistant"
        export += f"## {role}\n\n{msg['content']}\n\n---\n\n"
    
    return export

# ============================================
# INITIALIZE SESSION STATE
# ============================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """👋 **Xin chào! Tôi là HR AI Assistant**

📚 Tôi có thể trả lời câu hỏi về:
• HR Policies (30 câu)
• Leave Policies (20 câu)
• Compensation (25 câu)
• Onboarding (25 câu)
• Benefits (20 câu)
• Compliance (12 câu)

💡 **Hỏi tôi bất kỳ điều gì về HR!**"""
        }
    ]

if 'stats' not in st.session_state:
    st.session_state.stats = {
        'found': 0,
        'not_found': 0,
        'total_queries': 0,
        'session_start': datetime.now()
    }

if 'debug_mode' not in st.session_state:
    st.session_state.debug_mode = False

# ============================================
# SIDEBAR
# ============================================

with st.sidebar:
    st.markdown("### ⚙️ System Dashboard")
    
    # Database info
    try:
        from services.vector_db import get_vector_db
        vdb = get_vector_db()
        count = vdb.count('hr_policies')
        st.success(f"✅ ChromaDB: {count} documents")
        st.metric("📊 Questions", f"~{count//3}")
    except Exception as e:
        st.error("❌ Database Error")
        st.caption(str(e))
    
    st.markdown("---")
    
    # Stats
    st.markdown("### 📈 Session Stats")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("✅ Found", st.session_state.stats['found'])
    with col2:
        st.metric("❌ Not Found", st.session_state.stats['not_found'])
    
    if st.session_state.stats['total_queries'] > 0:
        accuracy = (st.session_state.stats['found'] / st.session_state.stats['total_queries']) * 100
        st.metric("🎯 Success Rate", f"{accuracy:.1f}%")
    
    # Session time
    duration = datetime.now() - st.session_state.stats['session_start']
    st.caption(f"⏱️ Session: {duration.seconds//60}m {duration.seconds%60}s")
    
    st.markdown("---")
    
    # Debug Mode Toggle
    st.markdown("### 🔧 Developer Tools")
    
    debug_mode = st.toggle(
        "Debug Mode",
        value=st.session_state.debug_mode,
        help="Show technical details (source, match score, etc.)"
    )
    st.session_state.debug_mode = debug_mode
    
    if debug_mode:
        st.info("🔍 Debug info will show in responses")
    
    st.markdown("---")
    
    # Export & Clear
    st.markdown("### 💾 Actions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Clear", use_container_width=True):
            st.session_state.messages = st.session_state.messages[:1]  # Keep welcome
            st.session_state.stats = {
                'found': 0,
                'not_found': 0,
                'total_queries': 0,
                'session_start': datetime.now()
            }
            st.rerun()
    
    with col2:
        export_data = export_chat_history()
        if export_data:
            st.download_button(
                "📥 Export",
                data=export_data,
                file_name=f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                mime="text/markdown",
                use_container_width=True
            )
        else:
            st.button("📥 Export", disabled=True, use_container_width=True)
    
    st.markdown("---")
    st.caption("💡 Toggle Debug Mode to see technical details")

# ============================================
# MAIN CHAT INTERFACE
# ============================================

st.title("💼 HR AI Agent")
st.caption("🔍 Knowledge Base Assistant | 🤖 Powered by ChromaDB + Sentence Transformers")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Hỏi về HR policies, leave, compensation..."):
    
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        with st.spinner("🔍 Searching knowledge base..."):
            vector_result = query_vector_db(prompt)
        
        # Update stats
        st.session_state.stats['total_queries'] += 1
        
        if vector_result['found']:
            # ✅ FOUND IN KNOWLEDGE BASE
            answer = vector_result['answer']
            source = vector_result['source']
            similarity = vector_result['similarity']
            original_q = vector_result.get('question', '')
            distance = vector_result.get('distance', 0)
            result_type = vector_result.get('type', 'main')
            
            # Build response
            response = f"📚 **Knowledge Base Answer:**\n\n{answer}"
            
            # Debug info (only if debug mode enabled)
            if st.session_state.debug_mode:
                response += f"\n\n---\n"
                response += f"**🔍 Debug Info:**\n"
                response += f"- 📄 Source: `{source}`\n"
                response += f"- 🎯 Match: {similarity}% (distance: {distance:.3f})\n"
                response += f"- 📋 Type: {result_type}\n"
                if original_q and original_q != prompt:
                    response += f"- 💡 Matched: \"{original_q}\"\n"
            
            message_placeholder.success(response)
            st.session_state.stats['found'] += 1
            
        else:
            # ❌ NOT FOUND
            response = """❌ **Không tìm thấy câu trả lời**

Câu hỏi không có trong knowledge base (132 câu).

💡 **Gợi ý:**
- Thử hỏi lại bằng cách khác
- Hỏi về: HR Policies, Leave, Compensation, Onboarding, Benefits, Compliance"""
            
            if 'error' in vector_result:
                response += f"\n\n⚠️ Error: {vector_result['error']}"
            
            message_placeholder.warning(response)
            st.session_state.stats['not_found'] += 1
        
        # Save to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

# ============================================
# FOOTER
# ============================================

st.markdown("---")

# Quick questions
with st.expander("💡 Câu hỏi mẫu (Click để xem)"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
**HR Policies**
- Công ty làm việc từ mấy giờ?
- Có được làm remote không?
- Làm thêm giờ được tính thế nào?
- Có chương trình mentor không?
        """)
    
    with col2:
        st.markdown("""
**Leave & Benefits**
- Công ty cho nghỉ phép bao nhiêu ngày?
- Nghỉ ốm có tính vào ngày phép không?
- Có CLB thể thao không?
- Có khám sức khỏe định kỳ không?
        """)
    
    with col3:
        st.markdown("""
**Compensation**
- Lương được trả vào ngày nào?
- Có hỗ trợ đi lại không?
- BHXH được đóng bao nhiêu %?
- Có bonus cuối năm không?
        """)

st.markdown("---")
st.caption("**HR AI Agent v2.0** | Knowledge Base Only | With Debug Mode & Chat Export | 100% Local")