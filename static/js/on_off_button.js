const onOffButton = document.getElementById('on-off-button');
const autoModeElement = document.getElementById('auto-mode');

const turnOn = () => {
  setInnerText('turn off');
  return fetch('/turnOn');
};

const turnOff = () => {
  setInnerText('turn on');
  return fetch('/turnOff');
};

let toggle = true;
let handleAutobutton_toggle = true;

const handleClick = async () => {
  if (toggle === true) {
    turnOn();
    toggle = false;
  } else {
    turnOff();
    toggle = true;
  }
};

const setInnerText = (text) => {
  onOffButton.innerText = text;
};

const turnOn_15s = () => {
  fetch('/turnOn');
  setTimeout(() => {
    fetch('/turnOff');
  }, 15000);
};

let autoModeTimer;

const checkPHValue = () => {
  if (PHSensorValue >= 7.5 && PHSensorValue <= 8.5) {
  } else if (PHSensorValue < 7.5) {
    turnOn_15s();
  } else if (PHSensorValue > 8.5) {
    turnOn_15s();
  }
};

const autoModeTimer_start = () => {
  autoModeTimer = setInterval(checkPHValue, 30000);
};

const handleAutobuttonClick = () => {
  onOffButton.classList.toggle('none');
  if (handleAutobutton_toggle === true) {
    autoModeElement.innerText = 'auto mode off';
    handleAutobutton_toggle = false;
    autoModeTimer_start();
  } else {
    turnOff();
    autoModeElement.innerText = 'auto mode on';
    handleAutobutton_toggle = true;
    clearInterval(autoModeTimer);
  }
};

const onOffButtonInit = () => {
  onOffButton.addEventListener('click', handleClick);
  autoModeElement.addEventListener('click', handleAutobuttonClick);
};

onOffButtonInit();
