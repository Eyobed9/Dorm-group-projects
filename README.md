# Influencer Meeting Chat Application

This project is a chat application built using Django, designed to facilitate communication among influencers. Below are the details regarding the structure and functionality of the application.

## Project Structure

```plaintext
influencermeeting
├── chat
│   ├── migrations
│   ├── templates
│   │   └── chat
│   │       └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── influencermeeting
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## Features

- **Real-time Chat**: Users can send and receive messages in real-time.
- **User Authentication**: Secure login and registration for users.
- **Admin Interface**: Manage chat data through the Django admin panel.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd influencermeeting
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

- Navigate to `http://127.0.0.1:8000/` to access the chat application.
- Use the provided interface to log in or register and start chatting.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.