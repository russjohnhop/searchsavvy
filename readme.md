# Search Savvy

## Video Demo:
https://youtu.be/QJlrogv3k5U

## Description
### Overview
Search Savvy is an online learning website designed for pay-per-click advertising professionals to upskill and advance their careers.

### How It Works
#### User Registration and Authentication
- Users can create accounts or log in using their credentials.
- Upon registration, users gain access to their personalized profiles and learning dashboards.

#### Course Selection and Enrollment
- Users can explore available courses, each designed to cover specific aspects of PPC advertising.
- After selecting a course of interest, users can enroll to start their learning journey.

#### Interactive Learning Modules
- Courses are divided into interactive learning modules, offering lessons and quizzes.
- Lessons provide in-depth content on various PPC topics, accompanied by text, images, and multimedia elements.

#### Quiz-Based Assessments
- Each module includes quizzes designed to assess users' understanding.
- Users can attempt quizzes to test their knowledge and gain immediate feedback on their performance.

#### Real-Time Interactions
- The frontend JavaScript code manages real-time interactions, presenting questions and receiving user answers.
- Users can select answers and submit responses, with the system providing instant feedback.

#### API Integration
- The platform integrates backend APIs to retrieve course, lesson, quiz, question, and answer data.
- APIs enable smooth interactions between the frontend and backend, ensuring up-to-date content delivery.

#### Skill Enhancement
- By participating in quizzes and engaging with course material, users enhance their knowledge and skills in PPC advertising.
- The platform's specialized focus ensures users gain expertise relevant to their professional domain.

#### User Interaction Analytics
- The backend captures user interaction data, allowing administrators to analyze user engagement and performance.
- Analytics aid in refining content and improving the learning experience.

#### User-Friendly Interface
- The frontend offers an intuitive and user-friendly interface, guiding users through lessons, quizzes, and assessments.
- Clear navigation and structured content ensure a seamless learning journey.

### Distinctiveness and Complexity
This project is an online learning site designed specifically for pay-per-click (PPC) advertising professionals. It offers a comprehensive quiz-based learning experience, allowing users to test and enhance their knowledge of PPC advertising concepts and strategies. The project features a dynamic front-end built using JavaScript and a back-end powered by Django, ensuring a robust and interactive learning environment.

This project presented unique challenges, such as handling complex JavaScript interactions for quizzes, designing a relational database, and exploring different API implementation methods in Django.

## File Structure

### Root Directory
- `requirements.txt`: Contains all the Python libraries required to run the Django server.

### Backend (`core/static/core`)
- `views.py`: Manages backend logic, including user authentication, course enrollment, lesson and quiz navigation, and API endpoints.
- `urls.py`: Contains URL patterns for the application.
- `models.py`: Defines the data models for the application.

### Frontend (`core/templates/core`)
- List each HTML template and its purpose.

### Frontend (`core/static/core`)
- `main.css`: Contains the main stylesheet for the application.
- `courses.js`: Manages the interactive quiz experience on the frontend.

## How to Run the Application Locally
To host this app on your local machine:
1. Run `python manage.py runserver` from the `/searchsavvy` directory.
2. Follow the link in your terminal or navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.
