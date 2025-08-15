Question Classifier

This project provides a Python script to classify user questions into three categories: factual, opinion, or math. It also includes a basic response generation for each type, with optional integration with OpenAI's GPT models for enhanced responses.

Features

•
Question Classification: Categorizes questions based on keywords.

•
Basic Response Generation: Provides generic responses for each question type.

•
OpenAI GPT Integration (Bonus): Leverages OpenAI's GPT-3.5-turbo for more dynamic and intelligent responses to factual and opinion-based questions.

Installation

1.
Clone the repository (or copy the question_classifier.py file):

2.
Install dependencies:

3.
Set up your OpenAI API Key (for bonus features):

Usage

To use the question classifier, run the question_classifier.py script:

Bash


python question_classifier.py


The script will demonstrate how to classify questions and generate responses.

Example:

Python


from question_classifier import classify_question, get_response

user_question = "What is the capital of France?"
q_type = classify_question(user_question)
response = get_response(q_type, user_question)
print(f"Question: {user_question}\nType: {q_type}\nResponse: {response}")

user_question = "Do you think pineapple belongs on pizza?"
q_type = classify_question(user_question)
response = get_response(q_type, user_question)
print(f"Question: {user_question}\nType: {q_type}\nResponse: {response}")

user_question = "What is 5 times 7?"
q_type = classify_question(user_question)
response = get_response(q_type, user_question)
print(f"Question: {user_question}\nType: {q_type}\nResponse: {response}")


How to Add API/LLM Support (Bonus Explanation)

The current implementation already includes basic OpenAI GPT integration. To further enhance this, you could:

•
Fine-tune a model: For more accurate classification or domain-specific responses, you could fine-tune a smaller language model on a custom dataset of questions and their classifications/answers.

•
Integrate with other LLMs: Explore other LLMs like Google's Gemini API, Hugging Face models, or local LLMs for different capabilities or cost-effectiveness.

•
Advanced NLP Libraries: Use more sophisticated NLP libraries (e.g., spaCy, NLTK with pre-trained models) for more robust entity extraction and intent recognition, which can improve classification accuracy.

•
Knowledge Graphs: For factual questions, integrate with knowledge graph APIs (e.g., Wikidata, DBpedia) to retrieve precise information.

•
Contextual Understanding: Implement a mechanism to maintain conversation history for better contextual understanding, allowing the agent to answer follow-up questions more effectively.

•
Error Handling and Fallbacks: Improve error handling for API calls and implement more graceful fallbacks when API calls fail or return irrelevant responses.

License

This project is licensed under the MIT License - see the LICENSE file for details.

