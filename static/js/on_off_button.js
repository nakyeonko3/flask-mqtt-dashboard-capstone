const onOffButton = document.getElementById('on-off-button');

const turnOn = () => {
  setInnerText('turn off');
  return fetch('/turnOn');
};

const turnOff = () => {
  setInnerText('turn on');
  return fetch('/turnOff');
};

let toggle = true;

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

const onOffButtonInit = () => {
  onOffButton.addEventListener('click', handleClick);
};

onOffButtonInit();
