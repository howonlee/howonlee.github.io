---
layout: page
title: Repeat Your Repeating Tasks A Prime Number Of Days
---

<style>
  .recurrence-chart {
    margin: 0 0 3rem;
    border: 1px solid #30343b;
    border-radius: 14px;
    background: #16181c;
    overflow-x: auto;
  }

  .recurrence-chart svg {
    display: block;
    width: 100%;
    min-width: 680px;
    height: auto;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }

  .recurrence-chart .chart-title {
    fill: #f2f2f2;
    font-size: 19px;
    font-weight: 650;
  }

  .recurrence-chart .chart-subtitle,
  .recurrence-chart .axis-label,
  .recurrence-chart .tick-label {
    fill: #999fa8;
  }

  .recurrence-chart .chart-subtitle { font-size: 12px; }
  .recurrence-chart .axis-label { font-size: 11px; }
  .recurrence-chart .tick-label { font-size: 10px; }
  .recurrence-chart .value-label { fill: #f2f2f2; font-size: 12px; font-weight: 650; }
  .recurrence-chart .grid-line { stroke: #2a2e35; stroke-width: 1; }
  .recurrence-chart .prime { fill: #62d6c5; }
  .recurrence-chart .composite { fill: #ff9d66; }

  @media (max-width: 600px) {
    .recurrence-chart { margin-bottom: 1.5rem; border-radius: 10px; }
  }
</style>

<div id="recurrence-raster" class="recurrence-chart" role="img" aria-label="Recurrence timelines for prime and highly composite task intervals over 120 cycles"></div>

<div id="collision-bars" class="recurrence-chart" role="img" aria-label="Pair collisions for tasks repeating after prime or highly composite numbers of days, weeks, months, and quarters"></div>

<div id="lcm-matrices" class="recurrence-chart" role="img" aria-label="Pairwise least common multiple matrices for prime and highly composite recurrence intervals"></div>

<script>
(() => {
  "use strict";

  const NS = "http://www.w3.org/2000/svg";
  const prime = [5, 7, 11, 13, 23, 47];
  const composite = [4, 6, 12, 24, 36, 48];
  const colors = { prime: "#62d6c5", composite: "#ff9d66" };

  function node(name, attrs = {}, content) {
    const el = document.createElementNS(NS, name);
    Object.entries(attrs).forEach(([key, value]) => el.setAttribute(key, value));
    if (content !== undefined) el.textContent = content;
    return el;
  }

  function svgFor(target, width, height, title) {
    const svg = node("svg", { viewBox: `0 0 ${width} ${height}`, "aria-hidden": "true" });
    svg.appendChild(node("title", {}, title));
    document.getElementById(target).appendChild(svg);
    return svg;
  }

  function text(svg, x, y, content, className, anchor = "start") {
    svg.appendChild(node("text", { x, y, class: className, "text-anchor": anchor }, content));
  }

  function gcd(a, b) {
    while (b) [a, b] = [b, a % b];
    return a;
  }

  function lcm(a, b) {
    return (a * b) / gcd(a, b);
  }

  function pairCollisions(intervals, horizon) {
    let collisions = 0;
    for (let cycle = 1; cycle <= horizon; cycle += 1) {
      const simultaneous = intervals.filter(period => cycle % period === 0).length;
      collisions += simultaneous * (simultaneous - 1) / 2;
    }
    return collisions;
  }

  function drawRaster() {
    const width = 760;
    const height = 430;
    const svg = svgFor("recurrence-raster", width, height, "First 120 recurrence cycles");
    const left = 76;
    const right = 26;
    const plotWidth = width - left - right;
    const x = cycle => left + cycle / 120 * plotWidth;

    text(svg, 28, 36, "First 120 recurrence cycles", "chart-title");
    text(svg, 28, 57, "Six tasks · all begin together · a collision marker grows with simultaneous tasks", "chart-subtitle");

    [0, 20, 40, 60, 80, 100, 120].forEach(tick => {
      svg.appendChild(node("line", { x1: x(tick), y1: 78, x2: x(tick), y2: 397, class: "grid-line" }));
      text(svg, x(tick), 414, tick, "tick-label", "middle");
    });

    const panels = [
      { name: "PRIME", intervals: prime, top: 89, color: colors.prime },
      { name: "HIGHLY COMPOSITE", intervals: composite, top: 247, color: colors.composite }
    ];

    panels.forEach(panel => {
      text(svg, 28, panel.top + 9, panel.name, "axis-label");
      panel.intervals.forEach((period, row) => {
        const cy = panel.top + 29 + row * 18;
        text(svg, left - 12, cy + 3, period, "tick-label", "end");
        for (let cycle = period; cycle <= 120; cycle += period) {
          svg.appendChild(node("circle", { cx: x(cycle), cy, r: 2.4, fill: panel.color, opacity: 0.82 }));
        }
      });

      for (let cycle = 1; cycle <= 120; cycle += 1) {
        const simultaneous = panel.intervals.filter(period => cycle % period === 0).length;
        if (simultaneous > 1) {
          svg.appendChild(node("circle", {
            cx: x(cycle), cy: panel.top + 140, r: 1.7 + simultaneous * 1.25,
            fill: panel.color, opacity: 0.9, stroke: "#16181c", "stroke-width": 1
          }));
        }
      }
      text(svg, left - 12, panel.top + 143, "×", "value-label", "end");
    });
  }

  function drawBars() {
    const width = 760;
    const height = 450;
    const svg = svgFor("collision-bars", width, height, "Simultaneous task-pair collisions across recurrence units");
    const cases = [
      { label: "days", horizon: 365, span: "1 year" },
      { label: "weeks", horizon: 520, span: "10 years" },
      { label: "months", horizon: 480, span: "40 years" },
      { label: "quarters", horizon: 400, span: "100 years" }
    ].map(item => ({
      ...item,
      prime: pairCollisions(prime, item.horizon),
      composite: pairCollisions(composite, item.horizon)
    }));

    text(svg, 28, 36, "Simultaneous task-pair collisions", "chart-title");
    text(svg, 28, 57, "One collision = one pair of tasks landing on the same cycle", "chart-subtitle");

    const left = 68;
    const top = 92;
    const bottom = 370;
    const plotHeight = bottom - top;
    const maxValue = Math.ceil(Math.max(...cases.map(item => item.composite)) / 50) * 50;
    const y = value => bottom - value / maxValue * plotHeight;

    for (let tick = 0; tick <= maxValue; tick += 50) {
      svg.appendChild(node("line", { x1: left, y1: y(tick), x2: 735, y2: y(tick), class: "grid-line" }));
      text(svg, left - 10, y(tick) + 4, tick, "tick-label", "end");
    }

    const groupWidth = (735 - left) / cases.length;
    const barWidth = 34;
    cases.forEach((item, index) => {
      const center = left + groupWidth * (index + 0.5);
      [
        { value: item.prime, offset: -barWidth - 3, color: colors.prime },
        { value: item.composite, offset: 3, color: colors.composite }
      ].forEach(bar => {
        const barY = y(bar.value);
        svg.appendChild(node("rect", {
          x: center + bar.offset, y: barY, width: barWidth, height: bottom - barY,
          rx: 4, fill: bar.color
        }));
        text(svg, center + bar.offset + barWidth / 2, barY - 8, bar.value, "value-label", "middle");
      });
      text(svg, center, 397, item.label, "value-label", "middle");
      text(svg, center, 415, item.span, "tick-label", "middle");
    });

    svg.appendChild(node("circle", { cx: 273, cy: 439, r: 5, fill: colors.prime }));
    text(svg, 284, 443, `prime  ${prime.join(" · ")}`, "axis-label");
    svg.appendChild(node("circle", { cx: 460, cy: 439, r: 5, fill: colors.composite }));
    text(svg, 471, 443, `highly composite  ${composite.join(" · ")}`, "axis-label");
  }

  function drawMatrices() {
    const width = 760;
    const height = 430;
    const svg = svgFor("lcm-matrices", width, height, "Pairwise least common multiple matrices");
    text(svg, 28, 36, "Cycles until each pair meets again", "chart-title");
    text(svg, 28, 57, "Pairwise least common multiple · brighter cells meet sooner", "chart-subtitle");

    const matrixSize = 258;
    const cell = 36;
    const panels = [
      { x: 64, name: "PRIME", intervals: prime, color: colors.prime },
      { x: 440, name: "HIGHLY COMPOSITE", intervals: composite, color: colors.composite }
    ];

    panels.forEach(panel => {
      const y0 = 116;
      text(svg, panel.x + matrixSize / 2, 88, panel.name, "axis-label", "middle");
      panel.intervals.forEach((period, index) => {
        text(svg, panel.x + 32 + index * cell + cell / 2, 108, period, "tick-label", "middle");
        text(svg, panel.x + 22, y0 + index * cell + 23, period, "tick-label", "end");
      });

      const values = [];
      panel.intervals.forEach((a, row) => panel.intervals.forEach((b, col) => {
        if (row !== col) values.push(lcm(a, b));
      }));
      const minLog = Math.log(Math.min(...values));
      const maxLog = Math.log(Math.max(...values));

      panel.intervals.forEach((a, row) => {
        panel.intervals.forEach((b, col) => {
          const value = row === col ? null : lcm(a, b);
          const intensity = value === null ? 0 : 0.18 + 0.72 * (1 - (Math.log(value) - minLog) / (maxLog - minLog));
          svg.appendChild(node("rect", {
            x: panel.x + 32 + col * cell, y: y0 + row * cell,
            width: cell - 2, height: cell - 2, rx: 4,
            fill: value === null ? "#202329" : panel.color,
            opacity: value === null ? 1 : intensity
          }));
          text(svg, panel.x + 32 + col * cell + (cell - 2) / 2, y0 + row * cell + 22,
            value === null ? "—" : value, value !== null && intensity > 0.52 ? "value-label" : "tick-label", "middle");
        });
      });

      const pairValues = [];
      for (let i = 0; i < panel.intervals.length; i += 1) {
        for (let j = i + 1; j < panel.intervals.length; j += 1) pairValues.push(lcm(panel.intervals[i], panel.intervals[j]));
      }
      const average = Math.round(pairValues.reduce((sum, value) => sum + value, 0) / pairValues.length);
      text(svg, panel.x + 140, 360, average, "chart-title", "middle");
      text(svg, panel.x + 140, 381, "mean cycles between pair meetings", "axis-label", "middle");
    });
  }

  drawRaster();
  drawBars();
  drawMatrices();
})();
</script>
