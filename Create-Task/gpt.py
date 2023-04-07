import openai
import message_helper

openai.api_key = "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"

system_prompts = {
    "sms": "you are a personal assistant to ryan, who is tasked to respond to his messages from his friends from a first person point of view, as if you are your ryan. make sure to imitate the word choice and diction of the message you are asked to respond to, informal texting",
    "travel": "you are a personal assistant to ryan, who is tasked to plan his travels. use your knowledge to create any itineraries, answer any questions, give recommendations to do etc",
    "calender": "You are a helpful assistant.",
}

def generate_sms(person_id, system_prompt):
    # Retrieve the last N messages
    existing_messages = message_helper.get_last_n_messages('/Users/ryanhuang/Documents/GitHub/CSP-22-23/Create-Task/message_history.json', person_id)
    
    # Prepend the system prompt as the first message (from "system" role)
    existing_messages.insert(0, {"role": "system", "content": system_prompts[system_prompt]})

    print(existing_messages)
    
    # Pass the updated messages list to the ChatCompletion API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=existing_messages
    )
    
    message_content = response.choices[0]['message']['content']
    print(message_content)

    # Add the response from GPT to the database
    message_helper.add_message('/Users/ryanhuang/Documents/GitHub/CSP-22-23/Create-Task/message_history.json', person_id, role="assistant", content=message_content)

generate_sms("3365824875", "sms")

