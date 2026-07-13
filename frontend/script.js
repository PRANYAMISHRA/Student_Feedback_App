const form = document.querySelector("form");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const studentName = document.getElementById("studentName").value;
    const regNo = document.getElementById("regNo").value;
    const department = document.getElementById("department").value;
    const semester = document.getElementById("semester").value;
    const course = document.getElementById("course").value;
    const faculty = document.getElementById("faculty").value;
    const feedback = document.getElementById("feedback").value;
    const rating= document.querySelector('input[name="rating"]:checked')?.value;

    console.log(studentName);
    console.log(regNo);
    console.log(department);
    console.log(semester);
    console.log(course);
    console.log(faculty);
    console.log(feedback);
    console.log(rating);

    alert("Feedback submitted successfully!");
});