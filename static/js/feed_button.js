const feedButton = document.getElementById('feed-button');
const autoFeedButton = document.getElementById('auto-feed-button');

let auto_toggle = true;

const servo_turnOn = () => {
  fetch('/servo_turnOn');
};

const autoFeedButton_toggle = () => {
  feedButton.classList.toggle('none');
  if (auto_toggle === true) {
    fetch('/servo_motor_auto_mode');
    auto_toggle = false;
    autoFeedButton.innerText = 'auto feed off';
  } else {
    fetch('/servo_motor_auto_mode_off');
    auto_toggle = true;
    autoFeedButton.innerText = 'auto feed on';
  }
};

const handleFeedButtonClick = () => {
  servo_turnOn();
};
//5초간 interrupt 걸어주기

const handleAutoFeedButtonClick = () => {
  autoFeedButton_toggle();
};

const initFeedButton = () => {
  feedButton.addEventListener('click', handleFeedButtonClick);
  autoFeedButton.addEventListener('click', handleAutoFeedButtonClick);
};

initFeedButton();
