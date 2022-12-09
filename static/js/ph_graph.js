(async () => {
  const data = {
    labels: [],
    datasets: [
      {
        label: 'ph',
        data: [],
        // borderColor: 'rgb(54,162,235)',
        borderColor: 'rgb(112, 108, 108)',
        backgroundColor: 'rgb(145,203,245)',
        borderWidth: 1,
      },
    ],
  };
  const ph_config = {
    type: 'line',
    data,
    options: {
      animation: false,
      interaction: {
        intersect: false,
      },
      scales: {
        x: {
          type: 'realtime',
          realtime: {
            onRefresh: (chart) => {
              chart.data.datasets.forEach(async (dataset) => {
                dataset.data.push({
                  x: Date.now(),
                  y: await getPHSensorData(),
                });
              });
            },
          },
        },
        y: { beginAtZero: true },
      },
    },
  };

  const myChart = new Chart(document.getElementById('phChart'), ph_config);
})();
