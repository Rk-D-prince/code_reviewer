import os
import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

google_ai_key = os.getenv("GOOGLE_API_KEY")


if not google_ai_key:
    st.error("Google API key is missing. Please set it as an environment variable.")
    st.stop()

def review_code(code):
    try:
       
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",  # Update with the correct field if needed
            google_api_key=google_ai_key
        )


        prompt_template = PromptTemplate(
            input_variables=["code"],
            template="Review the following Python code and identify potential bugs, errors, or areas for improvement. Provide a fixed code snippet if possible:\n```python\n{code}\n```"
        )

               llm_chain = LLMChain(llm=llm, prompt=prompt_template)

        
        review = llm_chain.run(code)
        return review

    except Exception as e:
        return f"Error during code review: {e}"


def main():
    st.title("Python Code Reviewer")
    st.write("Enter your Python code below, and this tool will review it for bugs, errors, or potential improvements.")

    code = st.text_area("Enter your Python code:")

    if st.button("Review Code"):
        if code.strip():  # Ensure code is not empty
            with st.spinner("Reviewing your code..."):
                review = review_code(code)
            st.write(review)
        else:
            st.warning("Please enter some Python code to review.")


if __name__ == "__main__":
    main()
