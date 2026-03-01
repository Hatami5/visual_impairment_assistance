# <h1 align="center">🤖 AI-Powered Visual Assistant for Visually Impaired People 👁️‍🗨️</h1>
<p align="center">
<b>Real-time obstacle detection and intelligent navigation guidance using AI and computer vision.</b><br>
Built and maintained by <a href="https://github.com/hatami5">Hassan Hatami</a> • AI\ML Engineer & LLm Specialist
</p>

<h2> Overview</h2>
<p>
<b>AI-Powered Visual Assistant</b> is an assistive system designed to help visually impaired individuals navigate their surroundings safely. 
The system uses <b>computer vision and deep learning models</b> to detect obstacles, analyze their position, and generate real-time 
audio instructions such as moving left, right, or stopping.
</p>

<blockquote>
Designed to enhance independence and safety for visually impaired individuals using intelligent decision-based navigation.
</blockquote>

<h2> Key Features</h2>
<ul>
    <li>👁️ <b>Real-Time Object Detection</b> — Detects obstacles using YOLO-based deep learning models.</li>
    <li>🧭 <b>Decision-Based Navigation</b> — Provides intelligent directions like move left, right, or stop.</li>
    <li>🔊 <b>Audio Guidance</b> — Converts navigation instructions into voice feedback.</li>
    <li>⚡ <b>Fast Processing</b> — Optimized for real-time performance and smooth navigation.</li>
    <li>🧠 <b>AI-Powered Perception</b> — Understands the environment instead of simple detection.</li>
</ul>

<h2> Tech Stack</h2>
<table>
<tr><th>Tool / Framework</th><th>Purpose</th></tr>
<tr><td><b>Python 3.8+</b></td><td>Core programming language</td></tr>
<tr><td><b>YOLO (Ultralytics)</b></td><td>Real-time object detection</td></tr>
<tr><td><b>OpenCV</b></td><td>Image processing and camera input</td></tr>
<tr><td><b>PyTorch</b></td><td>Deep learning model execution</td></tr>
<tr><td><b>Text-to-Speech (TTS)</b></td><td>Voice guidance for navigation</td></tr>
</table>

<h2> Setup Instructions</h2>
<h3>1️⃣ Clone the Repository</h3>
<pre><code>git clone https://github.com/hatami5/ai-visual-assistant.git
cd ai-visual-assistant</code></pre>

<h3>2️⃣ Install Dependencies</h3>
<pre><code>pip install ultralytics opencv-python torch pyttsx3</code></pre>

<h3>3️⃣ Run the System</h3>
<pre><code>python main.py</code></pre>

<h2> How to Use</h2>
<ol>
    <li>Run the system using <code>python main.py</code>.</li>
    <li>The camera will start capturing real-time video.</li>
    <li>The AI model detects obstacles in the environment.</li>
    <li>The system generates audio instructions for safe navigation.</li>
</ol>

<h2> Example Output</h2>
<p><b>Detected:</b> Person ahead</p>
<p><b>System Instruction:</b> Move right</p>

<h2> How It Works</h2>
<ol>
    <li>The camera captures real-time frames from the environment.</li>
    <li>The YOLO model detects objects and obstacles.</li>
    <li>A decision engine analyzes object position (left, center, right).</li>
    <li>The system generates safe navigation instructions.</li>
    <li>Text-to-Speech converts instructions into audio feedback.</li>
</ol>

<h2> Future Enhancements</h2>
<ul>
    <li>🌟 Integration with wearable devices (smart glasses).</li>
    <li>🌟 Depth estimation for accurate distance measurement.</li>
    <li>🌟 GPS support for outdoor navigation.</li>
    <li>🌟 Mobile application deployment.</li>
</ul>

<h2 align="center"> Author</h2>
<p align="center">
<b>Hassan Hatami</b><br>
LLm Specialist | AI Engineer | Researcher<br>
<a href="https://github.com/Hatami5">GitHub</a> • <a href="https://www.linkedin.com/in/yourlinkedin">LinkedIn</a>
</p>

<p align="center"> ⭐ <b>If you like this project, don’t forget to star the repo and share it!</b> ⭐ </p>
