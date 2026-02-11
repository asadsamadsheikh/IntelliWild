function toggleChat() {
    const bot = document.getElementById("chatbot");
    bot.style.display =
        bot.style.display === "none" || bot.style.display === ""
            ? "block"
            : "none";
}

function sendMessage() {
    const input = document.getElementById("userInput");
    const msg = input.value.trim();
    if (msg === "") return;

    const chatBody = document.getElementById("chatBody");

    chatBody.innerHTML += `<div class="user-message">${msg}</div>`;

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        chatBody.innerHTML += `<div class="bot-message">${data.reply}</div>`;
        chatBody.scrollTop = chatBody.scrollHeight;
    });

    input.value = "";
}
