// http://bl.ocks.org/jyucsiro/767539a876836e920e38bc80d2031ba7
function drawWordCloud(word_count){
    var svg_location = "#chart";
    var width = $(document).width();
    var height = $(document).height();
//    var width = 750;
//    var height = 500;

    var fill = d3.scale.category20();

    var word_entries = d3.entries(word_count);

    var xScale = d3.scale.linear()
        .domain([0, d3.max(word_entries, function(d) {
            return d.value;
        })
        ])
        .range([10,100]);

    d3.layout.cloud().size([width, height])
        .timeInterval(20)
        .words(word_entries)
        .fontSize(function(d) { return xScale(d.value); })
        .text(function(d) { return d.key; })
        .rotate(function() { return 0; })
//        .rotate(function() { return ~~(Math.random() * 2) * 90; })
        .font("Impact")
        .on("end", draw)
        .start();

    function draw(words) {
        d3.select(svg_location).append("svg")
            .attr("width", width)
            .attr("height", height)
            .append("g")
            .attr("transform", "translate(" + [width / 2, height / 2] + ")")
            .selectAll("text")
            .data(words)
            .enter().append("text")
            .style("font-size", function(d) { return xScale(d.value) + "px"; })
            .style("font-family", "Impact")
            .style("fill", function(d, i) { return fill(i); })
            .attr("text-anchor", "middle")
            .attr("transform", function(d) {
                return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
            })
            .text(function(d) { return d.key; });
    }

    d3.layout.cloud().stop();
}