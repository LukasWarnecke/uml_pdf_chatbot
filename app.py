import streamlit as st
from process_txt import load_text, search_text
from crewai_wrapper import CrewAIWrapper

# Initialize components
TEXT_FILE_PATH = "document.txt"  # Replace with the path to your .txt file
THRESHOLD = 0.5  # Similarity threshold for text matching
crew_ai = CrewAIWrapper(model_name="llama2")

# Load the text file
@st.cache(allow_output_mutation=True)
def load_document():
    return load_text(TEXT_FILE_PATH)

# Streamlit App
def main():
    st.title("PDF Chatbot - Exam Preparation Tool 📚")
    st.markdown(
        """
        **Instructions**:
        1. Type your question in the input box below.
        2. The chatbot will search the document and provide an answer based on the text.
        3. Cited references from the text will also be displayed.
        """
    )

    # User Input
    query = st.text_input("Enter your question:", placeholder="e.g., What is supervised learning?")
    if st.button("Get Answer") and query.strip():
        with st.spinner("Searching for answers..."):
            # Load document
            lines = load_document()

            # Search for relevant text
            matches = search_text(lines, query, threshold=THRESHOLD)
            matched_lines = [match[0] for match in matches]
            cited_references = [f"Line {match[1] + 1}: {match[0]}" for match in matches]

            # Generate response
            response = crew_ai.generate_response(query, matched_lines)

        # Display Results
        st.subheader("Answer:")
        st.write(response)

        st.subheader("Cited References:")
        if cited_references:
            st.write("\n".join(cited_references))
        else:
            st.write("No relevant information found in the document.")
    else:
        st.write("Please enter a question and click 'Get Answer'.")

if __name__ == "__main__":
    main()
