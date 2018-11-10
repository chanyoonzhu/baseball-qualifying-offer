$(function() {
    // load data
    $.ajax({
        type: 'GET',
        url: "http://127.0.0.1:5000/",
        dataType: 'jsonp',
        success: function(response){
            console.log(response);
            renderGraph(response);
        },
        error: function(result){
            console.log("Error");
        }
    })

    function renderGraph (salaryObj) {
        google.charts.load("current", {packages:["corechart"]});
        google.charts.setOnLoadCallback(drawChart);
        function drawChart() {
            var data = google.visualization.arrayToDataTable(salaryObj['table']);

            var options = {
            title: 'Lengths of dinosaurs, in meters',
            legend: { position: 'none' },
            };

            var chart = new google.visualization.Histogram(document.getElementById('chart_div'));
            chart.draw(data, options);
        }
    }
});