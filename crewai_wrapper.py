from crewai import CrewAI

class CrewAIWrapper:
    def __init__(self, model_name="llama2"):
        """
        Initialize the CrewAI model.
        Args:
        - model_name: Name of the open-source model to use (default: "llama2").
        """
        try:
            # Initialize the CrewAI instance
            self.model = CrewAI.load_model(model_name)
        except Exception as e:
            raise RuntimeError(f"Error loading CrewAI model: {e}")

    def generate_response(self, query, context):
        """
        Generate a response using the provided query and context.
        
        Args:
        - query: The user's input question.
        - context: List of lines retrieved from the text as context.
        
        Returns:
        - Generated response from the model.
        """
        if not context:
            return "I'm sorry, I couldn't find any relevant information in the document."
        
        # Format the context for the model
        formatted_context = "\n".join(context)
        prompt = (
            f"The following is context from a document:\n"
            f"{formatted_context}\n\n"
            f"Based on the above context, answer the following question:\n"
            f"{query}\n"
            f"Please cite relevant sections where applicable."
        )
        
        try:
            # Generate response
            response = self.model.generate(prompt, max_length=512)
            return response
        except Exception as e:
            return f"Error generating response: {e}"

# Example usage:
if __name__ == "__main__":
    # Initialize the CrewAI wrapper
    crewai = CrewAIWrapper(model_name="llama2")
    
    # Sample query and context
    query = "What is supervised learning?"
    context = [
        "Linear regression is a type of supervised learning.",
        "This section covers the basics of supervised learning."
    ]
    
    # Generate the response
    response = crewai.generate_response(query, context)
    
    # Print the response
    print(f"Query: {query}")
    print(f"Response: {response}")
