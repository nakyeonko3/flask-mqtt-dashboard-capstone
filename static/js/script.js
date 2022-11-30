console.log('hello world');

const submit_form = document.querySelector('.submit_form');
const sensor_data_div = document.querySelector('.sensor_data_div');
const date_div = document.querySelector('.date_div');

const init = () => {
  submit_form.addEventListener('submit', handleSubmit);
  renderSensorData();
  //   setInterval(renderSensorData, 1000);
  setInterval(renderNotDateTime, 1000);
};

const handleSubmit = (event) => {
  event.preventDefault();
  renderSensorData();
};

const getSensorData = () => {
  return fetch('/getSensorData')
    .then((response) => response.json())
    .then((data) => data.sensor_data);
};

const renderSensorData = async () => {
  sensor_data_div.innerText = await getSensorData();
};

const getNowDateTime = () => {
  const now = new Date();
  const locale = navigator.language;
  return new Intl.DateTimeFormat(locale, {
    dateStyle: 'medium',
    timeStyle: 'medium',
  }).format(now);
};

const renderNotDateTime = () => {
  date_div.innerText = getNowDateTime();
};
// 24시간에 한 번씩, 날짜 변경될 때만 날짜가 바뀌도록 수정해보기

init();
