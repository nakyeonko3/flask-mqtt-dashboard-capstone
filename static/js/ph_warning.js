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
  if (PHSensorValue < 7) {
    ph_warning_Element.innerText = '산성';
  } else if (PHSensorValue > 7) {
    ph_warning_Element.innerText = '염기성';
  } else {
    ph_warning_Element.innerText = '중성';
  }
};

const initPh = () => {
  setInterval(renderPHSensorValue, 1000);
};

initPh();
