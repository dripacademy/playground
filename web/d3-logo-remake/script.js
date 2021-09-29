const body = document.getElementsByTagName("body")[0]
const width = body.offsetWidth
const height = body.offsetHeight

const label = "DripAcademy™"

const svg = d3.select("svg");
svg.attr("viewBox", [0, 0, width, height])
   .attr("xmlns", "http://www.w3.org/2000/svg")
   .attr("font-family", "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif")
   .attr("font-size", "50px")

for (l in label) {
    svg.append("text")
       .attr("x", "200px")
       .attr("y", "200px")
       .attr("stroke", "black")
       .text(label[l])
}
