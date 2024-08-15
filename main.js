document.getElementById('assignmentForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const studentName = document.getElementById('studentName').value;
    const assignment = document.getElementById('assignment').value;
    const dueDate = document.getElementById('dueDate').value;
    
    const data = {
        studentName: studentName,
        assignment: assignment,
        dueDate: dueDate
    };
    
    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if(data.success) {
            alert('Assignment submitted successfully!');
        } else {
            alert('Error submitting assignment.');
        }
    })
    .catch(error => console.error('Error:', error));
});
