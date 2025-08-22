function speakText(text) {
    const synth = window.speechSynthesis;
    const utterance = new SpeechSynthesisUtterance(text);

    const voices = synth.getVoices();
    const preferredVoice = voices.find(voice => voice.name.includes("Male")) || voices[0];
    utterance.voice = preferredVoice;

    utterance.pitch = 1;
    utterance.rate = 1;
    utterance.volume = 1;

    synth.speak(utterance);
}

document.getElementById("generateBtn").addEventListener("click", async () => {
    const prompt = document.getElementById("prompt").value;
    const outputDiv = document.getElementById("output");

    outputDiv.textContent = "Generating story...";

    const response = await fetch("/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt })
    });

    const data = await response.json();
    if (data.story) {
        outputDiv.textContent = data.story;
        speakText(data.story);
    } else {
        outputDiv.textContent = "Error: " + (data.error || "Unknown error");
    }
});
