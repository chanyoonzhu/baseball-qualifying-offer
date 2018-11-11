$(function() {
    // load data
    $.ajax({
        type: 'GET',
        url: "https://mla-offer-api-heroku.herokuapp.com/fetch",
        dataType: 'jsonp',
        success: function(response){
            console.log(response)
            $title = $('#offer-title');
            $offer = $('#offer');
            $title.text('Qualifying Offer Value');
            $offer.text(response['offer']);
            renderGraph(response);
        },
        error: function(result){
            console.log("Error");
        }
    })

    function renderGraph (salaryObj) {
        google.charts.load("current", {packages:["corechart"]});
        google.charts.setOnLoadCallback(drawChart1);
        function drawChart1() {
            // params
            var year = salaryObj['year']
            var level = salaryObj['level']

            var data = google.visualization.arrayToDataTable(salaryObj['table']);

            var options = {
            title: year + ' ' + level + ' Salaries',
            titleTextStyle: {color: '#E81828'},
            legend: { position: 'none' },
            color: '#284898',
            hAxis: { gridlines: {color: '#E81828'}},
            };

            var chart = new google.visualization.Histogram(document.getElementById('chart1_div'));
            chart.draw(data, options);
        }

        google.charts.setOnLoadCallback(drawChart2);
        function drawChart2() {
            // params
            var year = salaryObj['year']
            var level = salaryObj['level']

            var data = google.visualization.arrayToDataTable(salaryObj['best']);

            var options = {
            title: year + ' ' + level + ' Top ' + (salaryObj['best'].length - 1) + ' Salaries',
            titleTextStyle: {color: '#E81828'},
            hAxis: { textPosition: 'none' },
            legend: { position: 'none' },
            color: '#284898',
            };

            var chart = new google.visualization.LineChart(document.getElementById('chart2_div'));
            chart.draw(data, options);
        }

        google.charts.setOnLoadCallback(drawChart3);
        function drawChart3() {

            var neighbors = salaryObj['neighbors'];
            var data = google.visualization.arrayToDataTable(neighbors);

            var options = {
            title: 'Salaries Close to Qualifying Offer',
            titleTextStyle: {color: '#E81828'},
            legend: { position: 'none' },
            color: '#284898',
            };

            var chart = new google.visualization.BarChart(document.getElementById('chart3_div'));
            chart.draw(data, options);
        }
    }
});