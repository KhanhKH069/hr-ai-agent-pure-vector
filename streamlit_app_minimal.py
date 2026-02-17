#!/usr/bin/env python3
"""
HR AI Agent
"""

import streamlit as st
import os
import sys
from dotenv import load_dotenv

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
load_dotenv()

st.set_page_config(
    page_title="HR AI Agent",
    page_icon="📚",
    layout="wide"
)

# ============================================
# HELPER FUNCTIONS
# ============================================

def validate_match(user_question, matched_question, distance):
    """
    Validate if the match is actually good
    Prevents returning wrong answers!
    """
    # If very similar (distance < 0.5), trust it
    if distance < 0.5:
        return True
    
    # For borderline matches (0.5-0.7), check keywords
    user_words = set(user_question.lower().split())
    matched_words = set(matched_question.lower().split())
    
    # Remove common stop words
    stop_words = {'là', 'có', 'được', 'không', 'gì', 'như', 'thế', 'nào', 'bao', 'nhiêu', 
                  'the', 'is', 'are', 'what', 'how', 'when', 'where'}
    user_words -= stop_words
    matched_words -= stop_words
    
    # Count common meaningful words
    common = user_words & matched_words
    
    # Need at least 1-2 common meaningful words for borderline matches
    if distance < 0.6:
        return len(common) >= 1  # Relaxed for good similarity
    else:
        return len(common) >= 2  # Strict for poor similarity

def query_vector_db(question):
    """Query ChromaDB with VALIDATION"""
    try:
        from services.vector_db import get_vector_db
        
        vdb = get_vector_db()
        results = vdb.query(
            collection_name='hr_policies',
            query_text=question,
            n_results=3  # Get top 3 to find best match
        )
        
        if results and results['documents'] and len(results['documents'][0]) > 0:
            # Try each result until we find a validated match
            for i in range(len(results['documents'][0])):
                metadata = results['metadatas'][0][i]
                distance = results['distances'][0][i] if 'distances' in results else 1.0
                
                # First check: distance threshold
                if distance >= 0.7:
                    continue
                
                # Second check: validate match quality
                matched_q = metadata.get('question', '')
                if not validate_match(question, matched_q, distance):
                    continue
                
                # Passed both checks!
                similarity = round((1 - distance) * 100, 1)
                
                return {
                    'found': True,
                    'answer': metadata.get('answer', ''),
                    'question': matched_q,
                    'source': metadata.get('source_file', 'Unknown'),
                    'similarity': similarity,
                    'distance': distance
                }
        
        return {'found': False}
        
    except Exception as e:
        st.error(f"❌ Lỗi: {e}")
        return {'found': False}

# ============================================
# PAGE
# ============================================

st.title("📚 HR AI Agent")
# Sidebar
with st.sidebar:
    st.markdown("### 📊 Database")
    
    try:
        from services.vector_db import get_vector_db
        vdb = get_vector_db()
        count = vdb.count('hr_policies')
        st.success(f"✅ ChromaDB: {count} docs")
        st.metric("Questions", f"~{count//3}")
    except:
        st.warning("⚠️ ChromaDB not loaded")
    
    st.markdown("---")
    st.markdown("### 📈 Stats")
    
    if 'stats' not in st.session_state:
        st.session_state.stats = {'found': 0, 'not_found': 0, 'wrong_avoided': 0}
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("✅ Found", st.session_state.stats['found'])
    with col2:
        st.metric("❌ Not Found", st.session_state.stats['not_found'])
    
    st.markdown("---")
    if st.button("🔄 Clear", use_container_width=True):
        st.session_state.messages = []
        st.session_state.stats = {'found': 0, 'not_found': 0, 'wrong_avoided': 0}
        st.rerun()

# Chat
st.markdown("### 💬 Chat")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 **Xin chào! Hỏi tôi nhé!**"}
    ]

if 'stats' not in st.session_state:
    st.session_state.stats = {'found': 0, 'not_found': 0, 'wrong_avoided': 0}

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Hỏi về HR..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        with st.spinner("🔍 Searching..."):
            vector_result = query_vector_db(prompt)
        
        if vector_result['found']:
            answer = vector_result['answer']
            source = vector_result['source']
            similarity = vector_result['similarity']
            original_q = vector_result.get('question', '')
            
            response = f"📚 **Knowledge Base:**\n\n{answer}\n\n---\n"
            response += f"📄 _Source: {source}_\n🎯 _Match: {similarity}%_"
            
            if original_q and original_q != prompt:
                response += f"\n💡 _Matched: \"{original_q}\"_"
            
            message_placeholder.success(response)
            st.session_state.stats['found'] += 1
            
        else:
            response = "❌ **Tôi không biết câu này**."
            message_placeholder.warning(response)
            st.session_state.stats['not_found'] += 1
        
        st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")
with st.expander("💡 Câu hỏi mẫu"):
    st.markdown("""
**HR Policies:**
- Công ty làm việc từ mấy giờ?
- Có được làm remote không?
- Làm thêm giờ được tính như thế nào?
- Có chương trình mentor không?

**Leave Policies:**
- Công ty cho nghỉ phép bao nhiêu ngày?
- Nghỉ ốm có tính vào ngày phép không?
- Nếu phải làm ngày lễ thì được gì?

**Compensation:**
- Lương được trả vào ngày nào?
- Có hỗ trợ đi lại không?
- BHXH được đóng bao nhiêu %?

**Benefits:**
- Có CLB thể thao không?
- Có khám sức khỏe định kỳ không?
- Có hỗ trợ gym không?

**Onboarding:**
- Ngày đầu cần mang gì?
- Tuần đầu làm gì?
- Tháng 2 có đánh giá không?
    """)
st.caption("**HR AI Agent** | Knowledge Base Only | With Answer Validation")