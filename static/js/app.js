
// get all regions for given alliance
var series = country_details.map(country => country.region)

// creates object with counts for each unique region
for (i = 0, counts = {}; i < series.length; i++) {
  var num = series[i];
  counts[num] = counts[num] ? counts[num] + 1 : 1;
}

// sort by values of regions, largest to smallest
sorted_counts = Object.fromEntries(
    Object.entries(counts).sort(([,a],[,b]) => b-a)
);  

// pie chart options
var options = {
    chart: {
        type: 'pie'
    },
    series: Object.values(sorted_counts),
    labels: Object.keys(sorted_counts)
    }
var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();
