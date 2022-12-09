const onOffButton = document.getElementById('on-off-button');

const turnOn = () => {
  return fetch('/turnOn');
};

const turnOff = () => {
  return fetch('/turnOff');
};

let toggle = true;

const handleClick = async () => {
  if (toggle === true) {
    setInnerText('turn off');
    turnOn();
    toggle = false;
  } else {
    setInnerText('turn on');
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
