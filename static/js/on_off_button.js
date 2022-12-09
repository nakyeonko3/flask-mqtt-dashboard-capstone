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
  console.log('clicked');
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

const handleAutobuttonClick = () => {
  onOffButton.classList.toggle('none');
  if (handleAutobutton_toggle === true) {
    if (PHSensorValue >= 7.5 && PHSensorValue <= 8.5) {
      turnOff();
    } else if (PHSensorValue < 7.5) {
      turnOn();
    } else if (PHSensorValue > 8.5) {
      turnOn();
    }
    handleAutobutton_toggle = false;
    autoModeElement.innerText = 'auto mode off';
  } else {
    turnOff();
    handleAutobutton_toggle = true;
    autoModeElement.innerText = 'auto mode on';
  }
};

const onOffButtonInit = () => {
  onOffButton.addEventListener('click', handleClick);
  autoModeElement.addEventListener('click', handleAutobuttonClick);
};

onOffButtonInit();
