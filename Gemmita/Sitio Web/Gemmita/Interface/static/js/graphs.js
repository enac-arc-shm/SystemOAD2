

$(document).ready(function () {
    const context1 = document.getElementById('canvas1').getContext('2d');
    const myChart1 = new Chart(context1, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Solicitudes DHCP de los últimos 5 meses',
                data: [],
                borderColor: '#576CBC',
                borderWidth: 1,
                borderSkipped: false,
                borderRadius: Number.MAX_VALUE,
            }]
        },
        options: {
            scales: {
                x: {
                    display: true,
                    title: {
                      display: true,
                      text: 'Mes',
                      color: '#0B2447',
                      font: {
                         size: 20,
                        weight: 'bold',
                        lineHeight: 1.2,
                      },
                      padding: {top: 20, left: 0, right: 0, bottom: 0}
                    }
                  },
                  y: {
                    display: true,
                    title: {
                      display: true,
                      text: '# Solicitudes',
                      color: '#0B2447',
                      font: {
                        size: 20,
                       weight: 'bold',
                       lineHeight: 1.2,
                     },
                     padding: {top: 20, left: 0, right: 0, bottom: 0}
                    }}
            }
        }
    });

    setInterval(() => {
        fetch('/chart-data1')
            .then(response => response.json())
            .then(data => {
                myChart1.data.labels = data.mes;
                myChart1.data.datasets[0].data = data.value;
                myChart1.update();
            });
    }, 1000);
    const context2 = document.getElementById('canvas2').getContext('2d');
    const myChart2 = new Chart(context2, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Asignaciones DHCP',
                data: [],
                borderColor: '#576CBC',
                borderWidth: 1,
                borderSkipped: false,
                borderRadius: Number.MAX_VALUE,

            }]
        },
        options: {
            scales: {
                x: {
                    display: true,
                    title: {
                      display: true,
                      text: 'Mes',
                      color: '#0B2447',
                      font: {
                         size: 18,
                        weight: 'bold',
                        lineHeight: 1.2,
                      },
                      padding: {top: 20, left: 0, right: 0, bottom: 0}
                    }
                  },
                  y: {
                    display: true,
                    title: {
                      display: true,
                      text: '# Asignaciones',
                      color: '#0B2447',
                      font: {
                        size: 18,
                       weight: 'bold',
                       lineHeight: 1.2,
                     },
                     padding: {top: 20, left: 0, right: 0, bottom: 0}
                    }}
            }
        }
    });

    setInterval(() => {
        fetch('/chart-data2')
            .then(response => response.json())
            .then(data => {
                myChart2.data.labels = data.mes;
                myChart2.data.datasets[0].data = data.value;
                myChart2.update();
            });
    }, 1000);

    const context3 = document.getElementById('canvas3').getContext('2d');
    const myChart3 = new Chart(context3, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Detenciones DNS',
                data: [],
                borderColor: '#146C94',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    display: true,
                    title: {
                      display: true,
                      text: 'Mes',
                      color: '#0B2447',
                      font: {
                         size: 18,
                        weight: 'bold',
                        lineHeight: 1.2,
                      },
                      padding: {top: 20, left: 0, right: 0, bottom: 0}
                    }
                  },
                  y: {
                    display: true,
                    title: {
                      display: true,
                      text: '# Detenciones',
                      color: '#0B2447',
                      font: {
                        size: 18,
                       weight: 'bold',
                       lineHeight: 1.2,
                     },
                     padding: {top: 20, left: 0, right: 0, bottom: 0}
                    }}
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
                label: 'Errores de resolución',
                data: [],
                borderColor: '#146C94',
                borderWidth: 1
            }]
        },
        
        options: {
            scales: {
                x: {
                    display: true,
                    title: {
                      display: true,
                      text: 'Mes',
                      color: '#0B2447',
                      font: {
                         size: 18,
                        weight: 'bold',
                        lineHeight: 1.2,
                      },
                      padding: {top: 20, left: 0, right: 0, bottom: 0}
                    }
                  },
                  y: {
                    display: true,
                    title: {
                      display: true,
                      text: '# Errores',
                      color: '#0B2447',
                      font: {
                        size: 18,
                       weight: 'bold',
                       lineHeight: 1.2,
                     },
                     padding: {top: 20, left: 0, right: 0, bottom: 0}
                    }}
            }
        }
    });

    setInterval(() => {
        fetch('/chart-data4')
            .then(response => response.json())
            .then(data => {
                myChart4.data.labels = data.mes;
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
                label: 'Respuesta con código 404',
                data: [],
                borderColor: '#635985',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    display: true,
                    title: {
                      display: true,
                      text: 'Mes',
                      color: '#0B2447',
                      font: {
                         size: 20,
                        weight: 'bold',
                        lineHeight: 1.2,
                      },
                      padding: {top: 20, left: 0, right: 0, bottom: 0}
                    }
                  },
                  y: {
                    display: true,
                    title: {
                      display: true,
                      text: '# Respuestas',
                      color: '#0B2447',
                      font: {
                        size: 20,
                       weight: 'bold',
                       lineHeight: 1.2,
                     },
                     padding: {top: 20, left: 0, right: 0, bottom: 0}
                    }}
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
                label: 'Respuesta con código 200',
                data: [],
                borderColor: '#635985',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    display: true,
                    title: {
                      display: true,
                      text: 'Mes',
                      color: '#0B2447',
                      font: {
                         size: 18,
                        weight: 'bold',
                        lineHeight: 1.2,
                      },
                      padding: {top: 20, left: 0, right: 0, bottom: 0}
                    }
                  },
                  y: {
                    display: true,
                    title: {
                      display: true,
                      text: '# Respuestas',
                      color: '#0B2447',
                      font: {
                        size: 18,
                       weight: 'bold',
                       lineHeight: 1.2,
                     },
                     padding: {top: 20, left: 0, right: 0, bottom: 0}
                    }}
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
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Actividad de usuarios FTP',
                data: [],
                borderColor: '#2E4F4F',
                borderWidth: 1,
                pointStyle: 'circle',
      pointRadius: 10,
      pointHoverRadius: 15
            }]
        },
        options: {
            scales: {
                x: {
                    display: true,
                    title: {
                      display: true,
                      text: 'Usuario',
                      color: '#0B2447',
                      font: {
                         size: 18,
                        weight: 'bold',
                        lineHeight: 1.2,
                      },
                      padding: {top: 20, left: 0, right: 0, bottom: 0}
                    }
                  },
                  y: {
                    display: true,
                    title: {
                      display: true,
                      text: '# Actividades realizadas',
                      color: '#0B2447',
                      font: {
                        size: 18,
                       weight: 'bold',
                       lineHeight: 1.2,
                     },
                     padding: {top: 20, left: 0, right: 0, bottom: 0}
                    }}
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
