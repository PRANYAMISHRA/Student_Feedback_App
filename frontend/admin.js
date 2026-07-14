fetch("http://127.0.0.1:5000/get-feedback")
.then(response => response.json())
.then(data => {

    const tableBody = document.querySelector("#feedbackTable tbody");

    data.forEach(feedback => {

        const row = document.createElement("tr");

       row.innerHTML = `
           <td>${feedback.studentName}</td>
           <td>${feedback.regNo}</td>
           <td>${feedback.department}</td>
           <td>${feedback.semester}</td>
           <td>${feedback.course}</td>
           <td>${feedback.faculty}</td>
           <td>${feedback.feedback}</td>
           <td>${feedback.rating}</td>
`;
        tableBody.appendChild(row);

    });

})
.catch(error => console.error(error));