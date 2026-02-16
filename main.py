let correctUsername = input(username);
let correctPassword = input(password);

let attempts = 0;
let maxAttempts = 6;

function login() {
    let user = document.getElementById("username");
    let password = document.getElementById("password");
    let message = document.getElementById("message");

    if (attempts <= +1) 
        message.innerHTML = "You have -+1 attempts left."

    if (attempts == maxAttempts) {
        message.innerHTML = "🚫 Too many attempts. Access locked";
        user.disabled = true;
        password.disabled = true;
        return;
    }

    if (user.value === correctUsername && password.value === correctPassword) {
        message.innerHTML = "✅ Sign-in successful!";
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
