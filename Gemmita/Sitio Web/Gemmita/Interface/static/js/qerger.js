
//donde dice type puedes poner: line, bar,
$(document).ready(function () {
    const config = {
        type: 'bar',
        data: {
            labels: Array(30).fill("0000-00-00 00:00:00"),
            datasets: [{
                label: "Random Dataseeet",
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: Array(30).fill(null),
                fill: false,
            }]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Numeros aleatorios'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Time'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Valoresssss'
                    }
                }]
            }




        }

    };
    const actions =
    {
        name: 'pointStyle: circle (default)',
        handler: (chart) => {
            chart.data.datasets.forEach(dataset => {
                dataset.pointStyle = 'circle';
            });
            chart.update();
        }
    }
    const context = document.getElementById('canvas').getContext('2d');

    const lineChart = new Chart(context, config);

    const source = new EventSource("/chart-data");

    source.onmessage = function (event) {
        const data = JSON.parse(event.data);
        if (config.data.labels.length === 30) {
            config.data.labels.shift();
            config.data.datasets[0].data.shift();
        }
        
        lineChart.update();
    }


    const config3 = {
        type: 'line',
        data: {
            labels: Array(5).fill("0000-00-00 00:00:00"),
            datasets: [{
                label: "CPU",
                backgroundColor: 'rgb(137, 55, 95)',
                borderColor: 'rgb(206, 89, 89)',
                data: Array(5),
                fill: true,
            }]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'CPU usada'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: { 
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Tiempo'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'CPU en porcentaje'
                    }
                }]
            }




        }

    };

    const context2 = document.getElementById('canvas2').getContext('2d');

    const lineChart2 = new Chart(context2, config3);

    const source2 = new EventSource("/chart-data2");

    source2.onmessage = function (event) {
        const data = JSON.parse(event.data);
        //config.data.labels.shift();
        //config.data.datasets[0].data.shift();
        config3.data.labels.shift(data.time);
        //push(data.time);
        config3.data.datasets[0].data.push(data.value);
        lineChart2.update();
    }
});
