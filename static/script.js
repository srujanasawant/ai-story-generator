// For audio version of story
// Inbuilt browser voice model
function speakText(text) {
    const synth = window.speechSynthesis;
    const utterance = new SpeechSynthesisUtterance(text);

    // Optional: Pick a voice
    const voices = synth.getVoices();
    const preferredVoice = voices.find(voice => voice.name.includes("Male")) || voices[0];
    utterance.voice = preferredVoice;

    utterance.pitch = 1; // 0–2
    utterance.rate = 1;  // 0.1–10
    utterance.volume = 1; // 0–1

    synth.speak(utterance);
}

document.getElementById("generateBtn").addEventListener("click", async () => {
    const prompt = document.getElementById("prompt").value;
    const outputDiv = document.getElementById("output");
    
    outputDiv.textContent = "Generating story...";
    
    const response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt })
    });
    
    const data = await response.json();
    if (data.story) {
        outputDiv.textContent = data.story;
    } else {
        outputDiv.textContent = "Error: " + (data.error || "Unknown error");
    }

    // Read it aloud
    speakText(data.story);
});

