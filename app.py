# # Streamlit web application
# import streamlit as st
# from rag_pipeline import answer_question

# # Page configuration
# st.set_page_config(
#     page_title="Employee Policy Assistant",
#     page_icon="🤖",
#     layout="centered"
# )

# # Title
# st.title("🤖 Intelligent Employee Policy Assistant")

# st.markdown(
#     "Ask questions about leave policies, travel reimbursement, work-from-home rules, and medical insurance."
# )

# # User input
# question = st.text_input(
#     "Enter your question"
# )

# # Generate response
# if st.button("Ask"):

#     if question.strip():

#         with st.spinner("Searching policies..."):

#             response = answer_question(question)

#         st.subheader("Answer")
#         st.success(response)

#     else:
#         st.warning("Please enter a question.")



# Professional Streamlit UI for Employee Policy Assistant
# Professional Streamlit UI for Employee Policy Assistant








# Professional Employee Policy Assistant UI

import streamlit as st
from rag_pipeline import answer_question

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Employee Policy Assistant",
    page_icon="🤎",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp{
    background:#FFF8F2;
}

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* Hero Section */
.hero{
    background:linear-gradient(135deg,#FAD7C4,#FFF2E7);
    padding:40px;
    border-radius:30px;
    text-align:center;
    box-shadow:0px 8px 20px rgba(0,0,0,0.08);
}

.hero h1{
    color:#4E342E;
    font-size:52px;
}

.hero p{
    color:#6D4C41;
    font-size:18px;
}

/* Feature Pills */
.pill{
    background:#FFE8D6;
    color:#5D4037;
    padding:12px;
    border-radius:25px;
    text-align:center;
    font-weight:600;
}

/* Example Cards */
.example{
    background:white;
    padding:18px;
    border-radius:18px;
    color:black;
    text-align:center;
    box-shadow:0px 3px 10px rgba(0,0,0,0.08);
    font-weight:500;
}

/* Ask Box */
.ask-box{
    background:#FFFDFB;
    padding:25px;
    border-radius:25px;
    box-shadow:0px 5px 18px rgba(0,0,0,0.08);
}

/* Answer Card */
.answer{
    background:white;
    padding:25px;
    border-radius:20px;
    border-left:7px solid #D8A47F;
    box-shadow:0px 5px 15px rgba(0,0,0,0.08);
    color:black;
    font-size:17px;
}

/* Footer */
.footer{
    text-align:center;
    color:#8D6E63;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Hero ----------------
st.markdown("""
<div class='hero'>
<h1>🤎 Employee Policy Assistant</h1>
<p>
Instant answers to HR policies, travel reimbursements,
medical insurance and work-from-home guidelines.
</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- Features ----------------
c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("<div class='pill'>⚡ Fast Retrieval</div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='pill'>🧠 AI Powered</div>", unsafe_allow_html=True)

with c3:
    st.markdown("<div class='pill'>📄 Multi Policy Search</div>", unsafe_allow_html=True)

with c4:
    st.markdown("<div class='pill'>🔍 Semantic Search</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- Example Questions ----------------
st.markdown(
    "<h3 style='color:black'>📌 Example Questions</h3>",
    unsafe_allow_html=True
)

col1,col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class='example'>
    How many casual leaves are available?
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class='example'>
    Can employees work from home?
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class='example'>
    How does travel reimbursement work?
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class='example'>
    Who is covered under medical insurance?
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------- Question Section ----------------
st.markdown("""
<div class='ask-box'>
<h2 style='color:black;text-align:center'>
💬 Ask Anything
</h2>
</div>
""", unsafe_allow_html=True)

question = st.text_input(
    "",
    placeholder="Example: Can employees work from home?"
)

# ---------------- Answer Generation ----------------
if st.button("✨ Get Answer", use_container_width=True):

    if question:
        # st.markdown(
        #     """
        #     <h4 style='color:black;text-align:center'>
        #     🔍 Searching policies...
        #     </h4>
        #     """,
        #     unsafe_allow_html=True
        # )


        # with st.spinner(""):
        #     response = answer_question(question)

        status = st.empty()

        status.markdown(
            """
            <h4 style='color:black;text-align:center'>
            🔍 Searching policies...
            </h4>
            """,
            unsafe_allow_html=True
        )

        response = answer_question(question)

        status.empty()

        st.write("")

        st.markdown(
        f"""
        <div class='answer'>
        {response}
        </div>
        """,
        unsafe_allow_html=True
        )

    else:
        st.warning("Please enter a question.")

# ---------------- Footer ----------------
st.write("")
st.write("")

st.markdown("""
<div class='footer'>
Built with 🤎 using Streamlit • FAISS • Sentence Transformers • TinyLlama
</div>
""", unsafe_allow_html=True)
