import streamlit as st
from utils import extract_pdf, create_vector_text

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

st.set_page_config(page_title="Resume Analyzer")
st.title("Resume Analyzer AI")

resume_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])
jd_text = st.text_area("Paste the Job Description here")


if st.button("Analyze Resume"):
    if resume_file and jd_text:
        # extract resume
        resume_text = extract_pdf(resume_file)

        # combine resume and job description
        combined_text = resume_text + "\n\n" + jd_text

        # create vector representation of the combined text
        vectorstore = create_vector_text(combined_text)
        retriever = vectorstore.as_retriever()

        # load the LLM model
        llm = Ollama(model="gemma:latest")

        # prompt template design
        prompt = ChatPromptTemplate.from_template(
            """
           You are an AI Resume Analyzer. Analyze the provided resume against the job description.

Context: {context}
Question: {question}

Provide:

1. **Skills Gap Analysis** — matched, partial, and missing skills.
2. **Missing Skills** — prioritize as High, Medium, Low.
3. **ATS Score (0–100)** — based on keywords, skills, experience, education, and ATS compatibility.
4. **10 Technical Interview Questions** — specifically based on the JD and resume.
5. **Resume Improvement Suggestions** — keywords, projects, skills, summary, and formatting.
6. **Job-Specific Resume Changes** — show what to add, remove, or modify.
7. **Overall Suitability** — percentage and short conclusion.
8. **Top 5 Action Items** — most important improvements before applying.

### Graphical Representation

Include visual data wherever possible:

* **ATS Score:** gauge/progress chart
* **Skill Match:** bar chart showing required vs matched skills
* **Skill Gap:** chart showing matched, partial, and missing skills
* **Category Scores:** visual comparison of major skill categories

Use only calculated data from the resume and JD. Never invent scores or information. If data is insufficient, state so clearly.

Keep the output concise, professional, and dashboard-friendly.

            """
        )

        chain = (
            {
                "context": retriever,
                "question": RunnablePassthrough(),
            }
            | prompt
            | llm
            | StrOutputParser()
        )

        response = chain.invoke("Analyze the resume and job description.")

        st.subheader("Analysis Result")
        st.write(response)
    else:
        st.warning("Please upload a resume and provide a job description before analyzing.")