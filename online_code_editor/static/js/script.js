function runCode() {
    const code = document.getElementById("code").value;

    fetch('/run-code/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").textContent = data.output;
    })
    .catch(error => {
        document.getElementById("output").textContent = "Error: " + error;
    });
}

function getCSRFToken() {
    let name = 'csrftoken';
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        document.cookie.split(';').forEach(function(c) {
            const cookie = c.trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            }
        });
    }
    return cookieValue;
}
