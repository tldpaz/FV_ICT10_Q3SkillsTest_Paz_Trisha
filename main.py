let correctUsername = "admin";
let correctPassword = "1234";

let attempts = 0;
let maxAttempts = 6;

function login() {
    let user = document.getElementById("username");
    let pass = document.getElementById("password");
    let message = document.getElementById("message");

    if (attempts >= maxAttempts) {
        message.innerHTML = "🚫 Too many attempts. Access locked.";
        user.disabled = true;
        pass.disabled = true;
        return;
    }

    if (user.value === correctUsername && pass.value === correctPassword) {
        message.innerHTML = "✅ Login successful!";
        message.style.color = "green";
    } else {
        attempts++;
        let remaining = maxAttempts - attempts;

        message.innerHTML = "❌ Incorrect. Attempts left: " + remaining;
        message.style.color = "red";

        if (attempts >= maxAttempts) {
            user.disabled = true;
            pass.disabled = true;
            message.innerHTML = "🚫 Too many attempts. Access locked.";
        }
    }
}
