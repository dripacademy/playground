var width = window.innerWidth
var height = window.innerHeight

const svg = d3.selectAll("svg")
    .attr("viewBox", [0, 0, width * 1.25, height * 1.25])
    .style("font", "20px sans-serif")

svg.append("text")
    .text("kiffen")
    .attr("font-size", "12px")
    .attr("color", "black")
    .attr("x", "10")
    .attr("y", "10")

function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}

document.addEventListener("keydown", (e) => {
    const r = getRandomArbitrary(0, 256).toFixed(0)
    const g = getRandomArbitrary(0, 256).toFixed(0)
    const b = getRandomArbitrary(0, 256).toFixed(0)

    svg.append("text")
        .text(e.key)
        .attr("x", getRandomArbitrary(0, width))
        .attr("y", getRandomArbitrary(0, height))
        .attr("fill", `rgb(${r},${g},${b})`)
})
