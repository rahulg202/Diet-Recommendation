import os
from flask import Flask, request, render_template
import logging
import re
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)


def format_output(text):
    """Convert Markdown bold syntax to HTML strong tags."""
    return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

# chatbot initialization
def initialise_diet_recommender():
    try:
        # chatbot prompt for diet recommendations
        create_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a diet recommendation assistant."),
                ("user", """
                Based on the following user information, recommend a diet plan that includes breakfast, lunch, dinner, and suggested workouts.
                - Age: {age}
                - Gender: {gender}
                - Height: {height}
                - Weight: {weight}
                - Primary health goal: {health_goal} 
                - Daily activity level: {activity_level}
                - Sleep per night: {sleep} 
                - Diet type: {diet_type} 
                - How often the person eats fast or processed food: {fast_food_frequency} 
                - Exercise frequency: {exercise_frequency} 
                - Meal Preferences: {meal_preference} 
                """)
            ]
        )

        
        llama_model = OllamaLLM(model="llama3")
        format_output_parser = StrOutputParser()

       
        diet_recommender_pipeline = create_prompt | llama_model | format_output_parser
        return diet_recommender_pipeline
    except Exception as e:
        logging.error(f"Failed to initialize diet recommender: {e}")
        raise


diet_recommender_pipeline = initialise_diet_recommender()

# route for home page
@app.route('/')
def index():
    return render_template('index.html')

# route for diet recommendation
@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == "POST":
        # Collecting form data
        input_data = {
            "age": request.form['age'],
            "gender": request.form['gender'],
            "height": request.form['height'],
            "weight": request.form['weight'],
            "health_goal": request.form['health_goal'],
            "activity_level": request.form['activity_level'],
            "sleep": request.form['sleep'],
            "diet_type": request.form['diet_type'],
            "fast_food_frequency": request.form['fast_food_frequency'],
            "exercise_frequency": request.form['exercise_frequency'],
            "meal_preference": request.form['meal_preference']
        }

        
        try:
            response = diet_recommender_pipeline.invoke(input_data)
            output = format_output(response)
        except Exception as e:
            logging.error(f"Error during diet recommendation: {e}")
            output = "Sorry, an error occurred while processing your request."

        return render_template('result.html', output=output)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
