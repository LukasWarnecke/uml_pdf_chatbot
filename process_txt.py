from fuzzywuzzy import fuzz

def load_text(file_path):
    """
    Load the text from a file.
    Each line in the text file is treated as a separate entry.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return [line.strip() for line in lines if line.strip()]
    except Exception as e:
        raise RuntimeError(f"Error loading text file: {e}")

def search_text(lines, query, threshold=0.5):
    """
    Search through the lines for a query and return matching lines.
    Uses fuzzy matching to identify relevant lines.
    
    Args:
    - lines: List of lines from the text.
    - query: The user's query string.
    - threshold: Minimum similarity ratio (0 to 1) to consider a line a match.
    
    Returns:
    - A list of tuples (line, index, similarity_score) for matching lines.
    """
    results = []
    
    for idx, line in enumerate(lines):
        similarity = fuzz.partial_ratio(query.lower(), line.lower()) / 100.0
        if similarity >= threshold:
            results.append((line, idx, similarity))
    
    # Sort results by similarity in descending order
    results.sort(key=lambda x: x[2], reverse=True)
    return results

# Example usage:
if __name__ == "__main__":
    # Path to the sample text file (replace with your actual file)
    file_path = "example.txt"
    
    # Load the text content
    lines = load_text(file_path)
    
    # Query from the user
    query = "What is supervised learning?"
    
    # Search the text for matching lines
    matches = search_text(lines, query)
    
    # Print the matches
    print(f"Query: {query}")
    for match in matches:
        print(f"Line {match[1]}: {match[0]} (Similarity: {match[2]:.2f})")
