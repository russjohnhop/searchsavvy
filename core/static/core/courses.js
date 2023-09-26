
const questionIds = [];

let correctAnswersCount = 0;
let currentQuestion = 1;

document.addEventListener('DOMContentLoaded', function() {
  resetQuiz();

  document.querySelector('#submit').addEventListener('click', function(event) {
      event.preventDefault();
      const editElement = event.target;
      const questionId = editElement.dataset.id;
      questionIds.push(questionId);
      isCorrect(questionId);
      nextQuestion(questionId);
  });

  document.querySelector('#retry').addEventListener('click', function(event) {
      event.preventDefault();
      const editElement = event.target;
      const courseId = editElement.dataset.id;
      retryQuiz(courseId);
  }); 
});

function isCorrect(questionId) {
    const selectedAnswerId = document.querySelector(`input[name="question${questionId}"]:checked`).value;
    const selectedAnswerIdAsNumber = parseInt(selectedAnswerId, 10);
    user_correct = false;

    fetch(`/api/answers/${questionId}`)
    .then(response => response.json())
    .then(answer => {

      const selectedAnswer = answer.find(answerObj => answerObj.id === selectedAnswerIdAsNumber);

      if (selectedAnswer) {
        console.log('Selected Answer:', selectedAnswer);
      } else {
        console.log('Answer with the selected ID not found.');
      }


    if (selectedAnswer.is_correct === true) {
        user_correct = true;
        correctAnswersCount += 1;
    }
    else {
        user_correct = false;
    }
})
.catch(error => {
    console.error(`isCorrect error occured: ${error}`);
})

}



function nextQuestion(questionId) {

  const newQuestionId = +questionId + 1;

  fetch(`/api/questions/${newQuestionId}`)
    .then(response => response.json())
    .then(questions => {
      const currentQuestion = questions.find(question => question.id === newQuestionId);
      const submitBtn = document.getElementById('submit');
      submitBtn.dataset.id = newQuestionId; 

      if (currentQuestion) {
        let questionElem = document.getElementById("question");
     
        questionElem.textContent = currentQuestion.text;
      } else {
        console.log("Question not found.");
      }

      return fetch(`/api/answers/${newQuestionId}`);
    })
    .then(response => {
      const contentType = response.headers.get('content-type');
      if (!contentType || !contentType.includes('application/json')) {
        throw new Error('Invalid Content-Type. Expected application/json.');
      }
      return response.json();
    })
    .then(answers => {
      const answersContainer = document.getElementById('answersContainer');
      answersContainer.innerHTML = ''; // Clear existing answers

    for (const answer of answers) {

      const divElement = document.createElement("div");
      divElement.setAttribute("class", "form-check mb-2")
      divElement.setAttribute("id", "answers")
      

      const inputElement = document.createElement("input");
      inputElement.setAttribute("type", "radio");
      inputElement.setAttribute("class", "form-check-input");
      inputElement.setAttribute("id", `answer${answer.id}`);
      inputElement.setAttribute("name", `question${answer.question_id}`);
      inputElement.setAttribute("value", `${answer.id}`);

      const labelElement = document.createElement("label");
      labelElement.setAttribute("class", "form-check-label");
      labelElement.setAttribute("for", `answer${answer.id}`);
      labelElement.innerText = answer.text;

      divElement.appendChild(inputElement);
      divElement.appendChild(labelElement);

      answersContainer.appendChild(divElement);
    }

      currentQuestion++;


      if (currentQuestion <= 5 && answers.length > 0) {
      } else {
        console.log("Running endQuiz()")
        endQuiz();
      }
    })
    .catch(error => {
      console.error(error);
    });
}

function resetQuiz() {
    questionIds.length = 0;
    correctAnswersCount = 0;
    currentQuestion = 1;
}

function endQuiz() {

    const answerDiv = document.getElementById("answersContainer");
    answerDiv.style.display = 'none';
    const question = document.getElementById("question");
    question.style.display = 'none';
    const submitBtn = document.getElementById("submit");
    submitBtn.style.display = 'none';
    const quizTitle = document.getElementById("quiz-title");
    const quizId = quizTitle.dataset.quizId;
    console.log(`quizID: ${quizId}`)
    const quizIdInt = parseInt(quizId, 10);
    console.log(`quizIdInt: ${quizIdInt}`)
    const csrfToken = getCookie('csrftoken');

    if (correctAnswersCount >= 4) {
        
        const successDiv = document.getElementById("success");
        successDiv.style.display = 'block';
        fetch(`/api/quiz/${quizIdInt}/`)
        .then(response => response.json())
        .then(course => {
            console.log(`course: ${course}`)
            const courseId = course.id;
            console.log(`courseId: ${courseId}`)
        fetch(`/api/enrollments/${courseId}`, {
            method: "PUT",
            headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
            },
            body: JSON.stringify({ completed: true }), // Set the completed status to true
        })
            .then(response => {
              console.log(`enrollment response: ${response}`)
            if (response.ok) {
                console.log("Enrollment updated successfully.");
            } else {
                console.error("Failed to update enrollment.");
            }
            })
            .catch(error => {
            console.error("Error updating enrollment:", error);
            });
        });

    }
    else {
        const failureDiv = document.getElementById("failure");
        failureDiv.style.display = 'block';

    }
}

function retryQuiz(course_id) {
  // reload page/quiz
  const quizURL = `/quiz/${course_id}`;

  window.location.href = quizURL;
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}
