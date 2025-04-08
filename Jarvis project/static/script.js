function sendCommand(command) {
    fetch("/command", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `command=${command}`,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("status").innerText = data.status;
    })
    .catch(error => {
        document.getElementById("status").innerText = "Error sending command.";
        console.error(error);
    });
}

function startListening() {
    document.getElementById("status").innerText = "Listening...";
    sendCommand("start_listening");
}