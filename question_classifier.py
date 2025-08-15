
import openai
import os

def classify_question(question):
    question = question.lower()
    if any(word in question for word in ["calculate", "solve", "math", "plus", "minus", "times", "divided by"]):
        return "math"
    elif any(word in question for word in ["do you think", "should we", "opinion", "feel about", "best", "worst"]):
        return "opinion"
    elif any(word in question for word in ["what is", "who is", "when was", "where is", "how many", "define", "explain", "who invented"]):
        return "factual"
    else:
        return "unknown"

def get_response(question_type, question):
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "dummy_key":
        if question_type == "factual":
            return f"That\"s a factual question. For example, if you asked \"What is the capital of France?\", the answer is Paris. (API key not set or invalid, providing generic response)"
        elif question_type == "opinion":
            return f"That\"s an opinion-based question. Opinions can vary greatly! (API key not set or invalid, providing generic response)"
        elif question_type == "math":
            return f"That\"s a math question. I can help you with calculations."
        else:
            return "I\"m not sure how to classify that question. Can you rephrase it?"

    if question_type == "factual":
        try:
            response = openai.chat.completions.create(
                model="gemini-2.5-flash",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that answers factual questions concisely."},
                    {"role": "user", "content": question}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"I apologize, but I couldn\"t fetch a factual answer at this moment. Error: {e}"
    elif question_type == "opinion":
        try:
            response = openai.chat.completions.create(
                model="gemini-2.5-flash",
                messages=[
                    {"role": "system", "content": "You are an AI that can offer a balanced perspective on opinion-based questions, stating that opinions can vary."},
                    {"role": "user", "content": question}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"I apologize, but I couldn\"t form an opinion at this moment. Error: {e}"
    elif question_type == "math":
        return f"That\"s a math question. While I can classify it, solving complex math problems is beyond my current capabilities. For simple calculations, you can use a calculator."
    else:
        return "I\"m not sure how to classify that question. Can you rephrase it?"

if __name__ == '__main__':
    # Example usage with API calls (requires OpenAI API key to be set as an environment variable)
    # For testing, you might want to comment out the API calls if you don\"t have a key set up.

    print("--- Testing Factual Question ---")
    user_question_factual = "What is the capital of France?"
    q_type_factual = classify_question(user_question_factual)
    print(f"\"{user_question_factual}\" is: {q_type_factual}. Response: {get_response(q_type_factual, user_question_factual)}")

    print("\n--- Testing Opinion Question ---")
    user_question_opinion = "Do you think AI will take over the world?"
    q_type_opinion = classify_question(user_question_opinion)
    print(f"\"{user_question_opinion}\" is: {q_type_opinion}. Response: {get_response(q_type_opinion, user_question_opinion)}")

    print("\n--- Testing Math Question ---")
    user_question_math = "Calculate 2 plus 2."
    q_type_math = classify_question(user_question_math)
    print(f"\"{user_question_math}\" is: {q_type_math}. Response: {get_response(q_type_math, user_question_math)}")

    print("\n--- Testing Unknown Question ---")
    user_question_unknown = "Tell me a story."
    q_type_unknown = classify_question(user_question_unknown)
    print(f"\"{user_question_unknown}\" is: {q_type_unknown}. Response: {get_response(q_type_unknown, user_question_unknown)}")


