fetch('/data')
    .then(response => response.json())
    .then(data => {
        const width = 800;
        const height = 400;

        const svg = d3.select('#chart')
            .append('svg')
            .attr('width', width)
            .attr('height', height);

        const xScale = d3.scaleBand()
            .domain(data.map(d => d.text))
            .range([0, width])
            .padding(0.1);

        const yScale = d3.scaleLinear()
            .domain([-1, 1])
            .range([height, 0]);

        svg.selectAll('rect')
            .data(data)
            .enter()
            .append('rect')
            .attr('x', d => xScale(d.text))
            .attr('y', d => yScale(d.sentiment))
            .attr('width', xScale.bandwidth())
            .attr('height', d => height - yScale(d.sentiment))
            .attr('fill', d => d.sentiment > 0 ? 'green' : 'red');
    });
