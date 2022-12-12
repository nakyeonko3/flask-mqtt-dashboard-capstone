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

const handleAutoTextToggle = () => {
  if (handleAutobutton_toggle === true) {
    autoModeElement.innerText = 'auto feed off';
    handleAutobutton_toggle = false;
    fetch('/auto_pump_turnOn');
  } else {
    autoModeElement.innerText = 'auto feed on';
    handleAutobutton_toggle = true;
    fetch('/auto_pump_turnOff');
  }
};

const handleAutobuttonClick = () => {
  onOffButton.classList.toggle('none');
  handleAutoTextToggle();
};

const onOffButtonInit = () => {
  onOffButton.addEventListener('click', handleClick);
  autoModeElement.addEventListener('click', handleAutobuttonClick);
};

onOffButtonInit();
