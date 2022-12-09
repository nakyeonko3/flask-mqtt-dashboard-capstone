const pH_value_Element = document.getElementById('pH_value');
const ph_warning_Element = document.getElementById('ph_warning');

let PHSensorValue = 0;

const getPHSensorData = () => {
  return fetch('/getPHSensorData')
    .then((response) => response.json())
    .then((data) => data.sensor_data);
};

const renderPHSensorValue = async () => {
  PHSensorValue = await getPHSensorData();
  pH_value_Element.innerText = PHSensorValue;
  phWarning(PHSensorValue);
};

const phWarning = (PHSensorValue) => {
  if (PHSensorValue >= 7.5 && PHSensorValue <= 8.5) {
    ph_warning_Element.innerText = '적정 ph';
  } else if (PHSensorValue < 7.5) {
    ph_warning_Element.innerText = '경고 ph가 너무 낮습니다..';
  } else if (PHSensorValue > 8.5) {
    ph_warning_Element.innerText = '경고 ph가 너무 높습니다..';
  }
};

// setInterval(() => {
//   if (PHSensorValue >= 7.5 && PHSensorValue <= 8.5) {
//     turnOff();
//     setTimeout(() => {
//       turnOn();
//     }, 15000);
//   } else if (PHSensorValue < 7.5) {
//     turnOn();
//     setTimeout(() => {
//       turnOff();
//     }, 15000);
//   } else if (PHSensorValue > 8.5) {
//     turnOn();
//   }
// }, 60000);

const initPh = () => {
  setInterval(renderPHSensorValue, 1000);
};

initPh();
