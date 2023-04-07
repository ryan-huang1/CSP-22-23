import json

def add_new_person_without_messages(file_path, person_id):
    # Read data from JSON file
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Check if the person_id already exists in the data
    if person_id in data:
        print(f"Person with ID {person_id} already exists in the database.")
    else:
        # Add the new person with an empty message history
        data[person_id] = []
    
    # Write updated data back to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage
new_person_id = "1234567890"

# Add a new person to the database without any messages
# add_new_person_without_messages('/Users/ryanhuang/Documents/GitHub/CSP-22-23/Create-Task/message_history.json', new_person_id)

def get_last_n_messages(file_path, person_id, n=7):
    # Read data from JSON file
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Check if the person_id exists in the data
    if person_id in data:
        # Get the message history of the person
        message_history = data[person_id]
        # Get the last n messages using slicing
        last_n_messages = message_history[-n:]
        # Return the last n messages
        return last_n_messages
    else:
        # Return an empty list if the person does not exist in the database
        return []

# Example usage
person_id = "3365824875"

# Get and print the last 7 messages of the person with the specified person_id
# last_7_messages = get_last_n_messages('/Users/ryanhuang/Documents/GitHub/CSP-22-23/Create-Task/message_history.json', person_id, n=7)
# print(last_7_messages)

def add_message(file_path, person_id, role, content):
    # Create the new message in the standard format
    new_message = {"role": role, "content": content}
    
    # Read data from JSON file
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Check if the person_id already exists in the data
    if person_id in data:
        # Append the new message to the person's existing message history
        data[person_id].append(new_message)
    else:
        # If the person_id does not exist, add the person with the new message as their first message
        data[person_id] = [new_message]
    
    # Write updated data back to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage
person_id = "3365824875"
role = "user"
content = "How are you today?"

# Add the new message to the database
# add_message('/Users/ryanhuang/Documents/GitHub/CSP-22-23/Create-Task/message_history.json', person_id, role, content)
