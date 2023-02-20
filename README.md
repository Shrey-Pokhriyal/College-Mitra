# College-Mitra
This is a web application for a college ERP portal built using HTML, CSS, Bootstrap, JavaScript, and Python Django for the backend. The app allows students, faculty, and administration to communicate with each other, share resources, and access various features and functionalities of the college.

## Features
- Student portal: The app provides a dedicated student portal where students can access their course materials, grades, attendance records, and other academic resources.
- Faculty portal: The app provides a dedicated faculty portal where faculty members can upload course materials, manage grades, and communicate with students.
- Admin portal: The app provides a dedicated admin portal where college administrators can manage student information, course offerings, and faculty information.
- Resource sharing: The app allows for the sharing of resources, such as notes, study materials, and assignments, among students and faculty members.
- Communication: The app provides various channels for communication, such as chat rooms, forums, and email, to facilitate intercommunication among students, faculty, and administration.

## Installation
To install and run the app, follow these steps:

- Clone the repository to your local machine.
- Install the required dependencies by running pip install -r requirements.txt.
- Create a .env file and add the necessary environment variables (e.g. database URL, API keys, etc.).
- Run the migrations using the command python manage.py migrate.
- Create a superuser to access the admin portal using the command python manage.py createsuperuser.
- Start the backend server by running python manage.py runserver.
- Open your web browser and navigate to http://localhost:3000 to view the app.
## Dependencies
### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript
### Backend
- Python 3.8+
- Django
- Django REST framework
- Django JWT
## Contributing
If you'd like to contribute to the project, please follow these steps:

- Fork the repository to your own GitHub account.
- Create a new branch with your changes.
- Make your changes and commit them to the new branch.
- Push the branch to your GitHub account.
- Submit a pull request from your branch to the master branch of the main repository.
### License
This project is licensed under the MIT License.
