(function() {

    // CONSTANTS

    // Color Palette
    var EMERALD_COLOR = '#2ecc71';
    var MIDNIGHT_BLUE_COLOR = '#2c3e50';
    var ALIZARIN_COLOR = '#e74c3c';
    var WISTERIA_COLOR = '#8e44ad';
    var GREEN_SEA_COLOR = '#16a085';
    var PETER_RIVER_COLOR = '#3498db';
    var CARROT_COLOR = '#e67e22';
    var SUN_FLOWER_COLOR = '#f1c40f';

    var COLOR_LIST = [MIDNIGHT_BLUE_COLOR, EMERALD_COLOR, ALIZARIN_COLOR, GREEN_SEA_COLOR, PETER_RIVER_COLOR, SUN_FLOWER_COLOR, WISTERIA_COLOR];

    // Converts a simple dict to list
    function convertDictToList(dict) {

        var lst = [];

        for (var key in dict) {
            var obj = {
                'label': key,
                'value': dict[key]
            };

            lst.push(obj);
        }

        return lst;
    }

    // URLS
    //var BASE_URL = "http://127.0.0.1:8000";
    var BASE_URL = "";
    var CANDIDATES_URL = BASE_URL + "/api/v1/candidate/?format=json";

    // Choices
    var GENDER_CHOICES = {
        'M': 'Male',
        'F': 'Female',
    };

    var ETHNICITY_CHOICES = {
        'H': 'Hispanic',
        'A': 'Asian',
        'AA': 'African-American',
        'AP': 'Asian/Pacific Islanders',
        'C': 'Caucasian',
        'O': 'Other',
    };

    // Default Params
    var DEFAULT_YEAR = 2014;
    var TRANSITION_DURATION = 800;

    // END CONSTANTS

    // This creats the student gender pie chart
    function createStudentGenderChart(selector, data) {

        var width = d3.select(selector).style('width').replace("px", "") / 1.5;
        var height = width;

        var color = d3.scale.ordinal()
            .range(COLOR_LIST);

        var canvas = d3.select(selector)
            .append('svg')
            .attr('width', width)
            .attr('height', height);

        var group = canvas.append('g')
            .attr('transform', 'translate(' + width / 2 + ',' + height / 2 + ')');

        var arc = d3.svg.arc()
            .innerRadius(0)
            .outerRadius(width / 2);

        var pie = d3.layout.pie()
            .value(function(d) { return d.value; });

        var arcs = group.selectAll('.arc')
            .data(pie(data))
            .enter()
            .append('g')
            .attr('class', 'arc');

        arcs.append('path')
            .attr('d', arc)
            .attr('fill', function(d, i) { return color(i); })
            .style('opacity', 0)
            .transition()
            .duration(TRANSITION_DURATION)
            .style('opacity', 1);

        arcs.append('text')
            .attr('transform', function(d) {
                return 'translate(' + arc.centroid(d) + ")"; })
            .attr('text-anchor', 'middle')
            .attr('font-size', '1.5em')
            .text(function(d) { return GENDER_CHOICES[d.data.label] + " ( " + d.data.value + " )"; });
    }

    // This creats the student ethnicity donut chart
    function createStudentEthnicityChart(selector, data) {

        var width = d3.select(selector).style('width').replace("px", "") / 1.5;
        var height = width;

        var color = d3.scale.ordinal()
            .range(COLOR_LIST);

        var canvas = d3.select(selector)
            .append('svg')
            .attr('width', width)
            .attr('height', height);

        var group = canvas.append('g')
            .attr('transform', 'translate(' + width / 2 + ',' + height / 2 + ')');

        var arc = d3.svg.arc()
            .innerRadius(width / 4)
            .outerRadius(width / 2);

        var pie = d3.layout.pie()
            .value(function(d) { return d.value; });

        var arcs = group.selectAll('.arc')
            .data(pie(data))
            .enter()
            .append('g')
            .attr('class', 'arc');

        arcs.append('path')
            .attr('d', arc)
            .attr('fill', function(d, i) { return color(i); })
            .style('opacity', 0)
            .transition()
            .duration(TRANSITION_DURATION)
            .style('opacity', 1);

        arcs.append('text')
            .attr('transform', function(d) {
                return 'translate(' + arc.centroid(d) + ")";
            })
            .attr('text-anchor', 'middle')
            .attr('font-size', '1.5em')
            .text(function(d) { return ETHNICITY_CHOICES[d.data.label]; });
    }

    // This creates the Student Scores Bar Chart
    function createStudentScoresChart(selector, data) {
        var histogram = d3.layout.histogram().bins(5)(data);

        var lengthArray = [];
        for (var i = 0; i < histogram.length; i++) {
            lengthArray.push(histogram[i]['length']);
        }

        var containerWidth = d3.select(selector).style('width').replace("px", "") / 1.5;
        var width = containerWidth * 0.9;
        var containerHeight = containerWidth;
        var height = containerHeight * 0.9;
        var barWidth = width / 5;

        var color = d3.scale.ordinal()
            .range(COLOR_LIST);

        var canvas = d3.select(selector)
            .append('svg')
            .attr('width', containerWidth)
            .attr('height', containerHeight);

        var widthScale = d3.scale.linear()
                .domain([Math.min.apply(null, data), Math.max.apply(null, data)])
                .range([0, width]);

        var heightScale = d3.scale.linear()
                .domain([0, Math.max.apply(null, lengthArray)])
                .range([0, height * 0.9]);

        var xAxis = d3.svg.axis()
            .scale(widthScale)
            .orient("bottom");

        canvas.append('g')
            .attr('class', 'axis')
            .attr('transform', 'translate(' + containerWidth * 0.05 + ',' + containerHeight * 0.9 + ')')
            .call(xAxis);

        var bars = canvas.selectAll('.bar')
            .data(histogram)
            .enter()
            .append('g')
            .attr('transform', 'translate(' + containerWidth * 0.05 + ',0)')
            .attr('class', 'bar');

        bars.append('rect')
            .attr('x', function(d, i) { return widthScale(d.x); })
            .attr('y', function(d) { return height; })
            .transition()
            .duration(TRANSITION_DURATION)
            .attr('y', function(d) { return height - heightScale(d.length); })
            .attr('width', barWidth)
            .attr('height', function(d) { return heightScale(d.length); })
            .attr('fill', function(d,i) { return color(i); });

        bars.append('text')
            .attr('x', function(d) { return widthScale(d.x) + (width / 10); })
            .attr('y', function(d) { return height - heightScale(d.length); })
            .text(function(d) { return d.length; })
            .style('opacity', 0)
            .transition()
            .duration(TRANSITION_DURATION)
            .style('opacity', 1);
    }

    // This creates the Student Department Bubble Chart
    function createStudentDepartmentsChart(selector, data) {
        var containerWidth = d3.select(selector).style('width').replace("px", "") / 1.5;
        var diameter = containerWidth;
        var color = d3.scale.ordinal()
            .range(COLOR_LIST);

        var bubble = d3.layout.pack()
            .sort(null)
            .size([diameter, diameter])
            .padding(1.5);

        var canvas = d3.select(selector)
            .append('svg')
            .attr('width', diameter)
            .attr('height', diameter)
            .attr('class', 'bubble');

        var node = canvas.selectAll('.node')
            .data(bubble.nodes({'children': data}))
            //.filter(function(d) { return !d.children; })
            .enter()
                .append('g')
                .attr('class', 'node')
                .attr('transform', function(d) {
                    return 'translate(' + d.x + ',' + d.y + ')';
                });

        node.append('title')
            .text(function(d) { return d.label; });

        node.append('circle')
            .style('fill', function(d, i) { return color(i); })
            .attr('r', 0)
            .transition()
            .duration(TRANSITION_DURATION)
            .attr('r', function(d) { return d.r; });


        node.append("text")
            .attr("dy", ".3em")
            .style("text-anchor", "middle")
            .text(function(d) { return d.label; });
    }

    // This creates the Department Gender Stacked Graph
    function createDepartmentGenderChart(selector, data) {
        var containerWidth = d3.select(selector).style('width').replace("px", "") / 1.5;
        var containerHeight = 240;

        var margin = {top: 20, right: 10, bottom: 30, left: 40};
        var width = containerWidth - margin.left - margin.right;
        var height = containerHeight - margin.top - margin.bottom;

        var x = d3.scale.ordinal()
            .rangeRoundBands([0, width], .1);

        var y = d3.scale.linear()
            .rangeRound([height, 0]);

        var color = d3.scale.ordinal()
            .range(COLOR_LIST);

        var xAxis = d3.svg.axis()
            .scale(x)
            .orient("bottom");

        var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left")
            .tickFormat(d3.format(".2s"));

        var canvas = d3.select(selector)
            .append('svg')
            .attr('width', width + margin.left + margin.right)
            .attr('height', height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        x.domain(data.map(function(d) { return d.label; }));
        y.domain([0, d3.max(data, function(d) {
            return d.value['M'] + d.value['F'];
        })]);

        var data_trans = data.map(function(d) {
            return {
                'label': d.label,
                'value': [
                    {
                        'name': 'Male',
                        'y0': 0,
                        'y1': d.value['M']
                    },
                    {
                        'name': 'Female',
                        'y0': d.value['M'],
                        'y1': d.value['M'] + d.value['F']
                    }
                ]
            };
        });

        // X Axis
        canvas.append("g")
            .attr("class", "xaxis")
            .attr("transform", "translate(0," + height + ")")
            .call(xAxis);

        // Y Axis
        canvas.append("g")
            .attr("class", "yaxis")
            .call(yAxis)
            .append("text")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end");

        // Create Depatment Groups
        var department = canvas.selectAll(".department")
            .data(data_trans)
            .enter()
            .append("g")
            .attr("class", "department")
            .attr("transform", function(d) { return "translate(" + x(d.label) + ",0)"; });

        // Create Stacks
        department.selectAll('rect')
            .data(function(d) { return d.value; })
            .enter()
            .append("rect")
            .attr("width", x.rangeBand())
            .attr("y", function(d) { return y(0); })
            .transition()
            .duration(TRANSITION_DURATION)
            .attr("y", function(d) { return y(d.y1); })
            .attr("height", function(d) { return y(d.y0) - y(d.y1); })
            .style("fill", function(d) { return color(d.name); });


        var legend = canvas.selectAll(".legend")
            .data(color.domain().slice().reverse())
            .enter()
            .append("g")
            .attr("class", "legend")
            .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

        legend.append("rect")
            .attr("x", width - 18)
            .attr("width", 18)
            .attr("height", 18)
            .style("fill", color);

        legend.append("text")
            .attr("x", width - 24)
            .attr("y", 9)
            .attr("dy", ".35em")
            .style("text-anchor", "end")
            .text(function(d) { return d; });
    }

    // This function reads the JSON file and creates sub lists
    function createSublists(data) {

        var genderList = {};
        var ethnicityList = {};
        var satScoresList = [];
        var departmentCandidateList = {};
        var departmentGenderList = {};

        for (var i = 0; i < data.length; i++) {

            if (data[i]['gender'] !== undefined) {

                if (genderList[data[i]['gender']] !== undefined) {
                    genderList[data[i]['gender']] += 1;
                } else {
                    genderList[data[i]['gender']] = 1;
                }
            }

            if (ethnicityList[data[i]['ethnicity']] !== undefined) {
                ethnicityList[data[i]['ethnicity']] += 1;
            } else {
                ethnicityList[data[i]['ethnicity']] = 1;
            }

            if (data[i]['qualifications'] !== undefined) {
                for (var j = 0; j < data[i]['qualifications'].length; j++) {
                    if (data[i]['qualifications'][j]['name'] === 'SAT') {
                        satScoresList.push(data[i]['qualifications'][j]['score']);
                    }
                }
            }

            if (data[i]['departments'] !== undefined) {
                for (var k = 0; k < data[i]['departments'].length; k++) {
                    var name = data[i]['departments'][k]['department']['name'];

                    if (departmentCandidateList[name] !== undefined) {
                        departmentCandidateList[name] += 1;
                    } else {
                        departmentCandidateList[name] = 1;
                    }

                    if (departmentGenderList[name] === undefined) {
                        departmentGenderList[name] = {
                            'M': 0,
                            'F': 0
                        };
                    }

                    if (data[i]['gender'] !== undefined) {
                        departmentGenderList[name][data[i]['gender']] += 1;
                    }
                }
            }
        }

        return {
            "genderList": convertDictToList(genderList),
            "ethnicityList": convertDictToList(ethnicityList),
            "satScoresList": satScoresList,
            "departmentCandidateList": convertDictToList(departmentCandidateList),
            "departmentGenderList": convertDictToList(departmentGenderList)
        };
    }

    // This function reloads the data for a year.
    function reloadData(year) {

        var candidates = [];

        // This is the callback which is called when the fetch is complete
        function doneFetch() {
            var sublists = createSublists(candidates);

            createStudentGenderChart('.student-gender-chart', sublists['genderList']);
            createStudentEthnicityChart('.student-enthnicty-chart', sublists['ethnicityList']);
            createStudentScoresChart('.student-scores-chart', sublists['satScoresList']);
            createStudentDepartmentsChart('.student-departments-chart', sublists['departmentCandidateList']);
            createDepartmentGenderChart('.department-gender-chart', sublists['departmentGenderList']);

            d3.select('.main').style('z-index', '1');
            d3.select('.loading').style('display', 'none');
        }

        // This function fetches data recursively until there is
        // nothing left to fetch
        function fetch(url) {

            d3.select('.main').style('z-index', '-1');
            d3.select('.loading').style('display', 'block');

            d3.json(url, function(data) {

                candidates = candidates.concat(data['objects']);

                if (data['meta'] !== undefined) {
                    if (data['meta']['next'] !== undefined) {
                        if (data['meta']['next'] !== null) {
                            next_url = BASE_URL + data['meta']['next'];
                            fetch(next_url);
                        } else {
                            doneFetch();
                        }
                    } else {
                        doneFetch();
                    }
                } else {
                    doneFetch();
                }
            });
        }

        var filter_url = '&admission_year=' + year;
        var fetch_url = CANDIDATES_URL + filter_url;

        //fetch_url = '/sampleData.json';
        fetch(fetch_url);
    }

    // When the select value is changed then reload
    d3.select('select').on('change', function() {
        var year = parseInt(this.options[this.options.selectedIndex].label);

        d3.selectAll('svg').remove();
        reloadData(year);
    });

    reloadData(DEFAULT_YEAR);
}());
