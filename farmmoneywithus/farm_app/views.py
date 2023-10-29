import json
import openai
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv('OPENAI_KEY')

@method_decorator(csrf_exempt, name='dispatch')
class FarmingDecisionView(View):
    def post(self, request):
        # Parse the request data
        data = json.loads(request.body)
        location = data.get('location')
        temperature = data.get('temperature')
        precipitation = data.get('precipitation')
        demand = data.get('demand')
        supply = data.get('supply')
        marketPrice = data.get('marketPrice')
        soilType = data.get('soilType')

        # Construct the user message based on the received data
        user_message_content = (
            f"Given the location is {location}, temperature is {temperature}, "
            f"precipitation is {precipitation}, market demand is {demand}, "
            f"supply is {supply}, market price is {marketPrice}, and soil type is {soilType}, "
            "what should I consider for the upcoming farming decisions?"
        )

        # Send the request to the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message_content}
            ],
            max_tokens=100
        )

        # Extract the assistant's reply from the API response
        assistant_reply = response['choices'][0]['message']['content']

        # Return the assistant's reply to the frontend
        return JsonResponse({'reply': assistant_reply})

    def get(self, request, step):
        # Construct the user message based on the farming step
        user_message_content = f"What should I do during the {step.replace('-', ' ')} phase?"

        # Send the request to the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message_content}
            ],
            max_tokens=100
        )

        # Extract the assistant's reply from the API response
        assistant_reply = response['choices'][0]['message']['content']

        # Return the assistant's reply to the frontend
        return JsonResponse({'reply': assistant_reply})

def home(request):
    return render(request, 'home.html')
