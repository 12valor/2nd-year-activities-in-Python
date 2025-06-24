document.getElementById("contactForm").addEventListener("submit", function(event) {
    event.preventDefault();
    document.getElementById("response").innerText = "Message Sent! We'll get back to you soon.";
});
