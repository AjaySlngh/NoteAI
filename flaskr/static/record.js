const startButton = document.getElementById('start-button');
const stopButton = document.getElementById('stop-button');


let audioContext;
let micStreamAudioSourceNode;
let audioWorkletNode;


startButton.addEventListener('click', async () => {
  // Check if the browser supports the required APIs
  if (!window.AudioContext || 
      !window.MediaStreamAudioSourceNode || 
      !window.AudioWorkletNode) {
    alert('Your browser does not support the required APIs');
    return;
  }


  // Request access to the user's microphone
  const micStream = await navigator
      .mediaDevices
      .getUserMedia({ audio: true });


  // Create the microphone stream
  audioContext = new AudioContext();
  mediaStreamAudioSourceNode = audioContext
      .createMediaStreamSource(micStream);


  // Create and connect AudioWorkletNode 
  // for processing the audio stream
  await audioContext
      .audioWorklet
      .addModule("my-audio-processor.js");
  audioWorkletNode = new AudioWorkletNode(
      audioContext,
      'my-audio-processor');
  micStreamAudioSourceNode.connect(audioWorkletNode);
});


stopButton.addEventListener('click', () => {
  // Close audio stream
  micStreamAudioSourceNode.disconnect();
  audioContext.close();
});

class MyAudioProcessor extends AudioWorkletProcessor {
    process(inputs, outputs, parameters) {
        // Get the input audio data from the first channel
        const inputData = inputs[0][0];


        // Do something with the audio data
        // ...
        
        return true;
    }
}


registerProcessor('my-audio-processor', MyAudioProcessor);
