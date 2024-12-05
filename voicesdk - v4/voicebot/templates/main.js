// main.js

let recorder;
let audioChunks = [];
let audioPlayer = document.getElementById('audioPlayer');

document.getElementById('startButton').addEventListener('click', startRecording);
document.getElementById('stopButton').addEventListener('click', stopRecording);
document.getElementById('processButton').addEventListener('click', processAudio);

async function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            recorder = new MediaRecorder(stream);
            recorder.ondataavailable = e => {
                audioChunks.push(e.data);
                if (recorder.state == 'inactive') {
                    document.getElementById('processButton').disabled = false;
                }
            };
            recorder.start();
            document.getElementById('startButton').disabled = true;
            document.getElementById('stopButton').disabled = false;
        })
        .catch(err => console.error('Error accessing microphone:', err));
}

function stopRecording() {
    recorder.stop();
    document.getElementById('startButton').disabled = false;
    document.getElementById('stopButton').disabled = true;
}

async function processAudio() {
    const blob = new Blob(audioChunks, { type: 'audio/wav' });
    const formData = new FormData();
    formData.append('audio', blob, 'recording.wav');

    try {
        const response = await fetch('/stream-conversation/', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        if (data.success) {
            audioPlayer.src = `/media/${data.audio_url}`;
            audioPlayer.play();
            document.getElementById('output').innerText = `LLM Response: ${data.message}`;
        } else {
            console.error('Error processing audio:', data.message);
            document.getElementById('output').innerText = 'Error processing audio.';
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('output').innerText = 'Error processing audio.';
    }

    // Reset audio chunks for next recording
    audioChunks = [];
}
