Search Savvy

Video Demo:
Description:
Overview:
My project is an online learning website for pay per click advertising professionals to upskill and develop their career.

How does it work?

User Registration and Authentication:

Users can create accounts or log in using their credentials.
Upon registration, users gain access to their personalized profiles and learning dashboards.

Course Selection and Enrollment:

Users can explore available courses, each designed to cover specific aspects of PPC advertising.
After selecting a course of interest, users can enroll to start their learning journey.

Interactive Learning Modules:

Courses are divided into interactive learning modules, offering lessons and quizzes.
Lessons provide in-depth content on various PPC topics, accompanied by text, images, and multimedia elements.

Quiz-Based Assessments:

Each module includes quizzes designed to assess users' understanding.
Users can attempt quizzes to test their knowledge and gain immediate feedback on their performance.

Real-Time Interactions:

The frontend JavaScript code manages real-time interactions, presenting questions and receiving user answers.
Users can select answers and submit responses, with the system providing instant feedback.

API Integration:

The platform integrates backend APIs to retrieve course, lesson, quiz, question, and answer data.
APIs enable smooth interactions between the frontend and backend, ensuring up-to-date content delivery.

Skill Enhancement:

By participating in quizzes and engaging with course material, users enhance their knowledge and skills in PPC advertising.
The platform's specialized focus ensures users gain expertise relevant to their professional domain.

User Interaction Analytics:

The backend captures user interaction data, allowing administrators to analyze user engagement and performance.
Analytics aid in refining content and improving the learning experience.

User-Friendly Interface:

The frontend offers an intuitive and user-friendly interface, guiding users through lessons, quizzes, and assessments.
Clear navigation and structured content ensure a seamless learning journey.
The Online Learning Site for Pay-Per-Click Advertising Professionals stands out by offering a dedicated platform for professionals to enhance their knowledge in a niche field. Its interactive quizzes, personalized tracking, and focused content make it a valuable resource for PPC advertising experts seeking to stay up-to-date with the latest industry trends and strategies.

Distinctiveness and Complexity:

This project is an online learning site designed specifically for pay-per-click (PPC) advertising professionals. It offers a comprehensive quiz-based learning experience, allowing users to test and enhance their knowledge of PPC advertising concepts and strategies. The project features a dynamic front-end built using JavaScript and a back-end powered by Django, ensuring a robust and interactive learning environment.

It is significantly different to an e-commerce site or social network - there were significant challenges. This was especially true for the JavaScript portion which took a long time, I wanted to do the entire quiz section with JS instead of using a Django view. This was more difficult but was a really valuable learning experience and further increased the complexity. I used DOM manipulation instead of doing the quiz portion on the back end, and utilised fetch to work with the backend. This part was much more difficult than the DOM manipulation in mail, and solidified my JS knowledge.

There were also lots of design decisions when it came to designing the database and models in Django. There were a greater amount of models at play and I had to be careful when managing their relationships. I also tried a new method of implementing APIs in Django using function-based views instead of class-based. I prefer class-based and would use that in future, but it was interested to see another way of doing it.

For the CSS, I chose to use Bootstrap. This was fairly new to me so required some additional learning to map out the overall structure.

What's contained in each file:

Root Directory:

requirements.txt: Contains all the Python libraries required to run the Django server.

Backend (core/static/core):

views.py: Manages backend logic, including user authentication, course enrollment, lesson and quiz navigation, and API endpoints.
urls.py: Contains URL patterns for the application.
models.py: Defines the data models for the application.

Frontend (core/templates/core):

List each HTML template and its purpose.

Frontend (core/static/core):

main.css: Contains the main stylesheet for the application.
courses.js: Manages the interactive quiz experience on the frontend.

How to run the application locally:

To host this app on your local machine, run python manage.py runserver from the "/searchsavvy" directory and follow the link in your terminal, or navigate to http://127.0.0.1:8000/ in your web browser.
