window.onload = function () {
    var chart = new CanvasJS.Chart("chartContainer",
    {
        title:{
            text: "Nutrition distribution"
        },
        legend: {
            maxWidth: 350,
            itemWidth: 120
        },
        data: [
        {
            type: "pie",
            showInLegend: true,
            legendText: "{indexLabel}",
            indexLabel: "{legendText}: {g}g ({y} %)",
            dataPoints: [
              {% for k, v in meals_list.percent.items %} 
                {% if v %}
                  { y: {{ v }}, g: "-",legendText: "{{ k }}" },
                {% endif %}
              {% endfor %}
            ]
        }
        ]
    });
    chart.render();
}

