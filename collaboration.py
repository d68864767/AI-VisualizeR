```python
# Import necessary libraries
from flask_socketio import join_room, leave_room

def handle_collaboration(collaboration_data):
    """
    This function handles collaboration requests. It allows users to join or leave a collaboration room.
    """

    # Extract the action and room from the collaboration data
    action = collaboration_data.get('action')
    room = collaboration_data.get('room')

    # If the action is 'join', add the user to the room
    if action == 'join':
        join_room(room)
        message = f'User has joined room {room}.'

    # If the action is 'leave', remove the user from the room
    elif action == 'leave':
        leave_room(room)
        message = f'User has left room {room}.'

    # If the action is not 'join' or 'leave', return an error message
    else:
        message = 'Error: Invalid action.'

    return message
```
