
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="I'm Sorry",
    page_icon="💗",
    layout="centered"
)

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Georgia, serif;
    text-align: center;
    color: #754253;
}

.stage {
    position: relative;
    width: 100%;
    max-width: 700px;
    height: 600px;
    margin: auto;
    overflow: hidden;
    border-radius: 22px;
    background: radial-gradient(circle, #fffafa, #ffe4ec);
}

.intro {
    position: absolute;
    top: 30px;
    width: 100%;
    z-index: 5;
}

.intro h2 {
    color: #d6336c;
    font-size: 25px;
}

.intro p {
    color: #986477;
}

.scene-svg {
    position: absolute;
    width: 100%;
    height: 100%;
    inset: 0;
}

#arrow {
    cursor: grab;
    touch-action: none;
    transform-origin: 0 0;
    transition: transform 0.85s ease-in;
}

#arrow:active {
    cursor: grabbing;
}

#heart {
    transform-box: fill-box;
    transform-origin: center;
    transition: transform .3s, opacity .3s;
}

#heart.burst {
    animation: heartBurst .55s forwards;
}

@keyframes heartBurst {
    0% { transform: scale(1); opacity: 1; }
    40% { transform: scale(1.5); opacity: 1; }
    100% { transform: scale(0); opacity: 0; }
}

.particle {
    opacity: 0;
    transform-box: fill-box;
    transform-origin: center;
}

.particle.burst {
    animation: spread .8s ease-out forwards;
}

@keyframes spread {
    0% {
        opacity: 1;
        transform: translate(0,0) scale(1);
    }
    100% {
        opacity: 0;
        transform: translate(var(--x),var(--y)) scale(.2);
    }
}

.hint {
    position: absolute;
    bottom: 25px;
    width: 100%;
    font-size: 16px;
    color: #754253;
}

.screen {
    display: none;
    position: absolute;
    inset: 0;
    align-items: center;
    justify-content: center;
    padding: 15px;
    background: linear-gradient(135deg,#fff1f5,#ffe0eb);
}

.screen.active {
    display: flex;
}

.panel {
    width: 100%;
    max-width: 520px;
    padding: 28px 15px;
    border-radius: 25px;
    background: rgba(255,255,255,.85);
    box-shadow: 0 10px 35px #d98da866;
}

.big-heart {
    font-size: 125px;
    animation: heartbeat 1s infinite;
}

@keyframes heartbeat {
    0%,100% {transform:scale(1)}
    50% {transform:scale(1.15)}
}

.question {
    font-size: clamp(27px,5vw,42px);
    color: #d6336c;
    font-weight: bold;
}

.panel p {
    color: #986477;
    font-size: 18px;
}

.buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    flex-wrap: wrap;
    min-height: 65px;
}

button {
    border: none;
    border-radius: 30px;
    padding: 14px 32px;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
}

#yes {
    background: #ed3976;
    color: white;
}

#no {
    background: #f5dce5;
    color: #754253;
}

.final-message {
    font-size: clamp(30px,6vw,48px);
    font-weight: bold;
    color: #d6336c;
}

.final-heart {
    font-size: 100px;
    animation: heartbeat 1s infinite;
}

@media(max-width:500px) {
    .stage {
        height: 550px;
    }
    .intro h2 {
        font-size: 21px;
    }
}
</style>
</head>

<body>

<div class="stage" id="stage">

    <!-- ARCHERY PAGE -->

    <section id="archery">

        <div class="intro">
            <h2>A little something for you 💗</h2>
            <p>Pull the arrow back and release it towards my heart.</p>
        </div>

        <svg class="scene-svg"
             viewBox="0 0 700 600"
             preserveAspectRatio="xMidYMid meet">

            <defs>
                <radialGradient id="pinkHeart">
                    <stop offset="0%" stop-color="#ff8bb5"/>
                    <stop offset="100%" stop-color="#e60055"/>
                </radialGradient>
            </defs>

            <!-- BOW STRING -->
            <line x1="125" y1="280"
                  x2="125" y2="515"
                  stroke="#d2b49c"
                  stroke-width="2"/>

            <!-- WOODEN CURVED BOW -->
            <path d="M125 280 Q45 397 125 515"
                  fill="none"
                  stroke="#70452d"
                  stroke-width="10"
                  stroke-linecap="round"/>

            <path d="M125 280 Q55 397 125 515"
                  fill="none"
                  stroke="#b47b4e"
                  stroke-width="3"/>

            <!-- BOW HANDLE -->
            <path d="M105 455 L138 478"
                  stroke="#59321e"
                  stroke-width="13"
                  stroke-linecap="round"/>

            <!-- HEART TARGET -->
            <g id="heart">

                <path d="M535 190
                         C465 125 405 200 535 320
                         C665 200 605 125 535 190Z"
                      fill="url(#pinkHeart)"
                      stroke="#ed6694"
                      stroke-width="3"/>

                <ellipse cx="505" cy="190"
                         rx="15" ry="10"
                         fill="white"
                         opacity=".65"/>

            </g>

            <!-- HEART BURST PARTICLES -->
            <g id="particles">

                <circle class="particle" cx="535" cy="210" r="8"
                        style="--x:90px;--y:-100px" fill="#ff4f91"/>

                <circle class="particle" cx="535" cy="210" r="9"
                        style="--x:-100px;--y:-90px" fill="#ff9fc2"/>

                <circle class="particle" cx="535" cy="210" r="7"
                        style="--x:110px;--y:50px" fill="#e60055"/>

                <circle class="particle" cx="535" cy="210" r="8"
                        style="--x:-100px;--y:70px" fill="#ff75a8"/>

                <circle class="particle" cx="535" cy="210" r="6"
                        style="--x:0px;--y:-140px" fill="#ffb6ce"/>

                <circle class="particle" cx="535" cy="210" r="7"
                        style="--x:0px;--y:130px" fill="#ed3976"/>

                <circle class="particle" cx="535" cy="210" r="8"
                        style="--x:145px;--y:-40px" fill="#ff9fc2"/>

                <circle class="particle" cx="535" cy="210" r="8"
                        style="--x:-145px;--y:-30px" fill="#e60055"/>

                <circle class="particle" cx="535" cy="210" r="6"
                        style="--x:80px;--y:110px" fill="#ff75a8"/>

                <circle class="particle" cx="535" cy="210" r="7"
                        style="--x:-80px;--y:110px" fill="#ffb6ce"/>

            </g>

            <!-- ARROW -->
            <g id="arrow" transform="translate(125 390) rotate(-32)">

                <!-- Arrow shaft -->
                <line x1="0" y1="0"
                      x2="270" y2="0"
                      stroke="#70452d"
                      stroke-width="5"
                      stroke-linecap="round"/>

                <!-- Arrowhead -->
                <path d="M270 0 L247 -12 L247 12 Z"
                      fill="#d6336c"/>

                <!-- Feathers -->
                <path d="M10 0 L-8 -15 L28 -5 Z"
                      fill="#e83e76"/>

                <path d="M10 0 L-8 15 L28 5 Z"
                      fill="#e83e76"/>

                <!-- Feather detail -->
                <line x1="5" y1="0"
                      x2="25" y2="-5"
                      stroke="#ffd0df"
                      stroke-width="2"/>

            </g>

        </svg>

        <div class="hint" id="hint">
            👇 Pull the arrow backwards and release!
        </div>

    </section>


    <!-- QUESTION PAGE -->

    <section id="questionScreen" class="screen">

        <div class="panel">

            <div class="big-heart">💘</div>

            <div class="question">
                Will you forgive me?
            </div>

            <p>It would mean a lot to me. 🥺</p>

            <div class="buttons">
                <button id="yes">YES ❤️</button>
                <button id="no">NO 🙈</button>
            </div>

        </div>

    </section>


    <!-- FINAL PAGE -->

    <section id="finalScreen" class="screen">

        <div class="panel">

            <div class="final-heart">❤️</div>

            <div class="final-message">
                I am very sorry!
            </div>

            <p>
                I truly mean it.
                I'm truly sorry for not understanding you and your feelings in that situation. I know I should have understood you better instead of reacting the way I did. I never wanted to hurt you, and I genuinely regret it. I promise I won't repeat the same mistake again. I'll try my best to understand you, listen to you, and be more careful with your feelings. Please forgive me. I'm really sorry, and I mean it from the bottom of my heart. ❤️🥺
                Thank you for giving me another chance. 💗
            </p>

            <div style="font-size:35px">
                🥹 💐 🫶
            </div>

        </div>

    </section>

</div>


<script>

const svg = document.querySelector('.scene-svg');
const arrow = document.getElementById('arrow');
const heart = document.getElementById('heart');
const particles = document.querySelectorAll('.particle');

const hint = document.getElementById('hint');

const archery = document.getElementById('archery');
const questionScreen = document.getElementById('questionScreen');
const finalScreen = document.getElementById('finalScreen');

let dragging = false;
let startX = 0;
let pulled = false;

function getSvgX(event) {
    const rect = svg.getBoundingClientRect();
    return (event.clientX - rect.left) * 700 / rect.width;
}

// Pull arrow backwards
arrow.addEventListener('pointerdown', (e) => {

    if (pulled) return;

    dragging = true;
    startX = getSvgX(e);

    arrow.style.transition = 'none';

    arrow.setPointerCapture(e.pointerId);

});

// Move arrow
arrow.addEventListener('pointermove', (e) => {

    if (!dragging) return;

    let dx = getSvgX(e) - startX;

    dx = Math.max(-90, Math.min(0, dx));

    arrow.setAttribute(
        'transform',
        `translate(${125 + dx} 390) rotate(-32)`
    );

});

// Release arrow and shoot
arrow.addEventListener('pointerup', () => {

    if (!dragging) return;

    dragging = false;
    pulled = true;

    hint.textContent = '❤️ Your arrow is on its way...';

    arrow.style.transition = 'transform .85s cubic-bezier(.2,.7,.3,1)';

    // Arrow flies towards the heart
    arrow.setAttribute(
        'transform',
        'translate(390 210) rotate(0)'
    );

    // Heart gets hit
    setTimeout(() => {

        hint.textContent = '💗 A message from my heart...';

        // Heart burst
        heart.classList.add('burst');

        particles.forEach((particle) => {
            particle.classList.add('burst');
        });

        // Show next page
        setTimeout(() => {

            archery.style.display = 'none';
            questionScreen.classList.add('active');

        }, 850);

    }, 850);

});

arrow.addEventListener('pointercancel', () => {
    dragging = false;
});


// NO button movement
const no = document.getElementById('no');

function moveNoButton() {

    const stageRect = document.getElementById('stage').getBoundingClientRect();

    no.style.position = 'fixed';

    const maxX = window.innerWidth - no.offsetWidth - 20;
    const maxY = window.innerHeight - no.offsetHeight - 20;

    no.style.left = Math.max(10, Math.random() * maxX) + 'px';
    no.style.top = Math.max(10, Math.random() * maxY) + 'px';

    no.style.zIndex = '1000';
}

no.addEventListener('pointerenter', moveNoButton);

no.addEventListener('click', (e) => {
    e.preventDefault();
    moveNoButton();
});


// YES button
document.getElementById('yes').addEventListener('click', () => {

    no.style.position = 'relative';
    no.style.left = '';
    no.style.top = '';
    no.style.zIndex = '';

    questionScreen.classList.remove('active');
    finalScreen.classList.add('active');

});

</script>

</body>
</html>
"""

components.html(html, height=620, scrolling=False)
