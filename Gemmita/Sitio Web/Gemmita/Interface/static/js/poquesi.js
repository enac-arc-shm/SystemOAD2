
/*$.getJSON('/chart-data3', function(data){

    const label= data.mes
    print(label)
    
    const config = {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Mi gráfica de línea',
                data: values,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    };

    const context5 = document.getElementById('canvas3').getContext('2d');

    const lineChart5 = new Chart(context5, config);
    data.forEach(function(point) {
        config.data.labels.push(data.mes);
        config.data.datasets[0].data.push(data.value);
    });
    lineChart5.update();
    
    //const chart = new Chart(document.getElementById('canvas3'), config);
});



;*/


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
        config.data.labels.push(data.time);
        config.data.datasets[0].data.push(data.value);
        lineChart.update();
    }


    const config3 = {
        type: 'line',
        data: {
            labels: Array(5).fill("0000/00/00 00:00:00"),
            datasets: [{
                label: "CPU",
                backgroundColor: 'rgb(137, 55, 95)',
                borderColor: 'rgb(206, 89, 89)',
                data: Array(5).fill(null),
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
        if (config3.data.labels.length === 5) {
            config3.data.labels.shift();
            config3.data.datasets[0].data.shift();
        }
        config3.data.labels.push(data.time);
        config3.data.datasets[0].data.push(data.value);
        //config3.data.labels.shift(data.time);
        //push(data.time);
        //config3.data.datasets[0].data.push(data.value);
        lineChart2.update();
    }
    //json={'mes : Dic': 'value :0', 'mes : Jan': 'value :0', 'mes : Feb': 'value :0', 'mes : Mar': 'value :0', 'mes : Apr': 'value :4'}


    /* const config4 = {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: "Código 404",
                backgroundColor: 'rgb(100, 55, 95)',
                borderColor: 'rgb(106, 50, 89)',
                data: [],
                fill: true,
            }]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Código 404'
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
                        labelString: 'Mes'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Respuestas'
                    }
                }]
            }
        }

    };

    const context3 = document.getElementById('canvas3').getContext('2d');

    const lineChart3 = new Chart(context3, config4);

    const source3 = new EventSource("/chart-data3");

    source3.onmessage = function (event) {
        const data = JSON.parse(event.data);
        //if (config4.data.labels.length === 5) {
        //    config4.data.labels.shift();
        //    config4.data.datasets[0].data.shift();
        //}
        config4.data.labels.push(data.mes);
        config4.data.datasets[0].data.push(data.value);
        //config3.data.labels.shift(data.time);
        //push(data.time);
        //config3.data.datasets[0].data.push(data.value);
        lineChart3.update();
    }
*/
    const config5 = {
        type: 'line',
        data: {
            labels: Array(5).fill("0000/00/00 00:00:00"),
            datasets: [{
                label: "CPU",
                backgroundColor: 'rgb(100, 60, 7)',
                borderColor: 'rgb(80, 50, 60)',
                data: Array(5).fill(null),
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
                        labelString: 'Tiempossiss'
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

    const context4 = document.getElementById('canvas4').getContext('2d');

    const lineChart4 = new Chart(context4, config5);

    const source4 = new EventSource("/chart-data4");

    source4.onmessage = function (event) {
        const data = JSON.parse(event.data);
        if (config5.data.labels.length === 5) {
            config5.data.labels.shift();
            config5.data.datasets[0].data.shift();
        }
        config5.data.labels.push(data.time);
        config5.data.datasets[0].data.push(data.value);
        //config3.data.labels.shift(data.time);
        //push(data.time);
        //config3.data.datasets[0].data.push(data.value);
        lineChart4.update();
    }



});
----------------
fetch('/chart-data3')
.then(response => response.json())
.then(data => {
  const ctx = document.getElementById('canvas3porqueya').getContext('2d');
  const myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: data.mes,
      datasets: [{
        label: 'My Dataset',
        data: data.value,
        borderColor: 'rgb(255, 99, 132)',
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        xAxes: [{
          type: 'time'
        }]
      }
    }
  });
});
------------------

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
        config.data.labels.push(data.time);
        config.data.datasets[0].data.push(data.value);
        lineChart.update();
    }


    const config2 = {
        type: 'line',
        data: {
            labels: Array(5).fill("0000/00/00 00:00:00"),
            datasets: [{
                label: "CPU",
                backgroundColor: 'rgb(137, 55, 95)',
                borderColor: 'rgb(206, 89, 89)',
                data: Array(5).fill(null),
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

    const lineChart2 = new Chart(context2, config2);

    const source2 = new EventSource("/chart-data2");

    source2.onmessage = function (event) {
        const data = JSON.parse(event.data);
        if (config2.data.labels.length === 5) {
            config2.data.labels.shift();
            config2.data.datasets[0].data.shift();
        }
        config2.data.labels.push(data.time);
        config2.data.datasets[0].data.push(data.value);
        //config3.data.labels.shift(data.time);
        //push(data.time);
        //config3.data.datasets[0].data.push(data.value);
        lineChart2.update();
    }
    //json={'mes : Dic': 'value :0', 'mes : Jan': 'value :0', 'mes : Feb': 'value :0', 'mes : Mar': 'value :0', 'mes : Apr': 'value :4'}


    /* const config4 = {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: "Código 404",
                backgroundColor: 'rgb(100, 55, 95)',
                borderColor: 'rgb(106, 50, 89)',
                data: [],
                fill: true,
            }]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Código 404'
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
                        labelString: 'Mes'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Respuestas'
                    }
                }]
            }
        }

    };

    const context3 = document.getElementById('canvas3').getContext('2d');

    const lineChart3 = new Chart(context3, config4);

    const source3 = new EventSource("/chart-data3");

    source3.onmessage = function (event) {
        const data = JSON.parse(event.data);
        //if (config4.data.labels.length === 5) {
        //    config4.data.labels.shift();
        //    config4.data.datasets[0].data.shift();
        //}
        config4.data.labels.push(data.mes);
        config4.data.datasets[0].data.push(data.value);
        //config3.data.labels.shift(data.time);
        //push(data.time);
        //config3.data.datasets[0].data.push(data.value);
        lineChart3.update();
    }

    const config5 = {
        type: 'line',
        data: {
            labels: Array(5).fill("0000/00/00 00:00:00"),
            datasets: [{
                label: "CPU",
                backgroundColor: 'rgb(100, 60, 7)',
                borderColor: 'rgb(80, 50, 60)',
                data: Array(5).fill(null),
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
                        labelString: 'Tiempossiss'
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

    const context4 = document.getElementById('canvas4').getContext('2d');

    const lineChart4 = new Chart(context4, config5);

    const source4 = new EventSource("/chart-data4");

    source4.onmessage = function (event) {
        const data = JSON.parse(event.data);
        if (config5.data.labels.length === 5) {
            config5.data.labels.shift();
            config5.data.datasets[0].data.shift();
        }
        config5.data.labels.push(data.time);
        config5.data.datasets[0].data.push(data.value);
        //config3.data.labels.shift(data.time);
        //push(data.time);
        //config3.data.datasets[0].data.push(data.value);
        lineChart4.update();
    }

   */
    const context3 = document.getElementById('canvas3').getContext('2d');
    const myChart3 = new Chart(context3, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'My Dataset',
                data: [],
                borderColor: 'rgb(255, 99, 132)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    type: 'time'
                }]
            }
        }
    });

    setInterval(() => {
        fetch('/chart-data3')
            .then(response => response.json())
            .then(data => {
                myChart3.data.labels = data.mes;
                myChart3.data.datasets[0].data = data.value;
                myChart3.update();
            });
    }, 1000);


    const context4 = document.getElementById('canvas4').getContext('2d');
    const myChart4 = new Chart(context4, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'My Dataset',
                data: [],
                borderColor: 'rgb(255, 99, 132)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    type: 'time'
                }]
            }
        }
    });

    setInterval(() => {
        fetch('/chart-data4')
            .then(response => response.json())
            .then(data => {
                myChart4.data.labels = data.dias;
                myChart4.data.datasets[0].data = data.value;
                myChart4.update();
            });
    }, 1000);


    const context5 = document.getElementById('canvas5').getContext('2d');
    const myChart5 = new Chart(context5, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'My Dataset',
                data: [],
                borderColor: 'rgb(255, 99, 132)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    type: 'time'
                }]
            }
        }
    });

    setInterval(() => {
        fetch('/chart-data5')
            .then(response => response.json())
            .then(data => {
                myChart5.data.labels = data.mes;
                myChart5.data.datasets[0].data = data.value;
                myChart5.update();
            });
    }, 1000);

    const context6 = document.getElementById('canvas6').getContext('2d');
    const myChart6 = new Chart(context6, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'My Dataset',
                data: [],
                borderColor: 'rgb(255, 99, 132)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    type: 'time'
                }]
            }
        }
    });

    setInterval(() => {
        fetch('/chart-data6')
            .then(response => response.json())
            .then(data => {
                myChart6.data.labels = data.mes;
                myChart6.data.datasets[0].data = data.value;
                myChart6.update();
            });
    }, 1000);

    const context7 = document.getElementById('canvas7').getContext('2d');
    const myChart7 = new Chart(context7, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'My Dataset',
                data: [],
                borderColor: 'rgb(255, 99, 132)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    type: 'time'
                }]
            }
        }
    });

    setInterval(() => {
        fetch('/chart-data7')
            .then(response => response.json())
            .then(data => {
                myChart7.data.labels = data.user;
                myChart7.data.datasets[0].data = data.value;
                myChart7.update();
            });
    }, 1000);

});
-----------
@app.route('/chart-data')
#Aquí se mandan los datos para generar una grafica con numeros aleatorios
def chart_data():
    def generate_random_data():
        while True:
            json_data = json.dumps(
                {
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                    'value': random.random() * 100})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
    return response


    --------------
    @app.route('/chart-data2')
#Aquí se mandan los datos para generar una grafica con el porcentaje de CPU usada, la cual se manda cada 4 segundos
def chart_data2():
    def display_usage(cpu_usage,mem_usage,bars=50):
        cpu_use = (cpu_usage) 
        mem_use = (mem_usage/100.0)     
        return cpu_use
    def generate_random_data2():
        while True:
            cpuu=psutil.cpu_percent()
           # print(cpuu)
            json_data2 = json.dumps(
                {
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                    'value': cpuu})
            yield f"data:{json_data2}\n\n"
            time.sleep(5)

    response = Response(stream_with_context(generate_random_data2()), mimetype="text/event-stream")
    return response