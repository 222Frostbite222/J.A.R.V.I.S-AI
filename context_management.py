
# Importing required libraries
import json

# Class for handling conversation context
class ContextManager:
    def __init__(self):
        self.context = {}

    def load_context(self):
        try:
            with open("conversation_context.json", "r") as file:
                self.context = json.load(file)
        except FileNotFoundError:
            pass

    def save_context(self):
        with open("conversation_context.json", "w") as file:
            json.dump(self.context, file)

    def update_context(self, key, value):
        self.context[key] = value
        self.save_context()

    def get_context(self, key):
        return self.context.get(key, None)

# Main function to demonstrate context management functionalities
def main():
    # Initialize Context Manager
    context_manager = ContextManager()
    
    # Load existing context
    context_manager.load_context()
    
    # Update context with new information
    context_manager.update_context('last_search_query', 'climate change')
    
    # Retrieve a specific context item
    last_search_query = context_manager.get_context('last_search_query')
    print(f"Last search query from context: {last_search_query}")

# Entry point of the program
if __name__ == "__main__":
    main()
