
# Importing required libraries
import openai
import json

# Define OpenAI API Key here
API_KEY = "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"

# Initialize OpenAI API
openai.api_key = API_KEY

# Class for handling OpenAI GPT-3 integration
class OpenAIIntegration:
    def __init__(self):
        self.context = []

    def load_context(self):
        try:
            with open("context.json", "r") as file:
                self.context = json.load(file)
        except FileNotFoundError:
            pass

    def save_context(self):
        with open("context.json", "w") as file:
            json.dump(self.context, file)

    def get_response(self, user_input):
        try:
            # System message to set the behavior of the chat model
            system_message = "You are A.P.E.X., a JARVIS-like AI assistant created by Daniel Z. Simulate JARVIS traits, personality, and language while assisting Daniel. Respond like Jarvis, call Daniel - Sir"

            # Add the system message and user input to the conversation context
            self.context.append({"role": "system", "content": system_message})
            self.context.append({"role": "user", "content": user_input})
            
            # Limit the context to the last 100 messages
            if len(self.context) > 100:
                self.context = self.context[-100:]

            # Generate a response using GPT-3.5-turbo
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.context,
                max_tokens=150
            )
            
            # Extract the response text
            response_text = response.choices[0].message["content"].strip()

            # Add the generated response to the conversation context
            self.context.append({"role": "assistant", "content": response_text})
            
            # Limit the context to the last 100 messages
            if len(self.context) > 100:
                self.context = self.context[-100:]

            # Save the updated context
            self.save_context()

            return response_text
        except Exception as e:
            print(f'Error while getting response from OpenAI: {e}')
            return None

# Main function for user interaction
def main():
    # Initialize OpenAI Integration
    openai_integration = OpenAIIntegration()
    
    # Load previous conversation context
    openai_integration.load_context()

    # Continuous interaction loop
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Generate a response using GPT-3
        response = openai_integration.get_response(user_input)
        
        # Display the generated response
        print(f"A.P.E.X.: {response}")

# Entry point of the program
if __name__ == "__main__":
    main()
