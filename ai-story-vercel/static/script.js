document.getElementById("generate").addEventListener("click", async () => {
    const prompt = document.getElementById("prompt").value.trim();
    if (!prompt) {
        alert("Please enter a prompt.");
        return;
    }

    try {
        const response = await fetch("/api/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt })
        });

        const data = await response.json();
        if (response.ok) {
            document.getElementById("story").innerText = data.story;
        } else {
            document.getElementById("story").innerText = `Error: ${data.error}`;
        }
    } catch (error) {
        document.getElementById("story").innerText = `Error: ${error.message}`;
    }
});
