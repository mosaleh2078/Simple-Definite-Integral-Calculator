<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Definite Integral Calculator</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 2em auto;">

<h1>🧮 Definite Integral Calculator (Midpoint Rule)</h1>

<p>This Python program approximates the <strong>definite integral</strong> of a single-variable mathematical function over a user-defined range using the <strong>Midpoint Riemann Sum</strong> method.</p>

<hr>

<h2>📦 How to Use</h2>

<ol>
    <li>Ensure Python 3.6+ is installed along with <code>numpy</code> and <code>colorama</code> packages.</li>
    <li>Save your function (e.g., <code>x**2 + 3*x + 2</code>) in a text file like <code>equation.txt</code>.</li>
    <li>Run the program:
        <pre><code>python main.py</code></pre>
    </li>
    <li>Follow the prompts:
        <ul>
            <li>Enter the range of integration (e.g., <code>1 5</code>)</li>
            <li>Enter a constant bound <code>k</code> such that <code>|f''(x)| ≤ k</code></li>
            <li>Provide the filename containing the function</li>
        </ul>
    </li>
</ol>

<p>The program will calculate and print the approximate integral result.</p>

<hr>

<h2>📐 Method Used</h2>

<p>The code uses the <strong>Midpoint Riemann Sum</strong> for numerical integration:</p>

<pre>
∫<sub>a</sub><sup>b</sup> f(x) dx ≈ Σ f(m<sub>i</sub>) × Δx
</pre>

<ul>
    <li>Δx = (b - a) / n</li>
    <li>Each m<sub>i</sub> is the midpoint of subinterval [x<sub>i</sub>, x<sub>i+1</sub>]</li>
</ul>

<p>The number of intervals <code>n</code> is calculated based on error tolerance:</p>

<pre>
n = ceil( sqrt( (k × (b - a)) / 0.00024 ) )
</pre>

<hr>

<h2>⚠️ Limitations</h2>

<ul>
    <li>Only supports <strong>single-line equations</strong>.</li>
    <li>Function evaluation uses Python <code>eval()</code> — do not use untrusted input.</li>
    <li>By default, expressions like <code>sin(x)</code> or <code>log(x)</code> aren't recognized unless <code>math</code> functions are exposed.</li>
</ul>

<hr>

<h2>📝 Equation File Format</h2>

<p>The equation file must contain one valid Python expression using variable <code>x</code>.</p>

<p><strong>Example:</strong></p>

<pre><code>x**2 + 3*x + 2</code></pre>

<hr>

<h2>📋 Requirements</h2>

<ul>
    <li>Python 3.6+</li>
    <li><code>numpy</code></li>
    <li><code>colorama</code></li>
</ul>

<p>Install dependencies with:</p>
<pre><code>pip install numpy colorama</code></pre>

<hr>

<h2>📄 License</h2>

<p>This project is free for educational and non-commercial use. No warranty is provided.</p>

<hr>

<h2>✍️ Author</h2>

<p>Created by <strong>Mohammad Saleh</strong> — 
<a href="mailto:mosaleh2078@gmail.com">mosaleh2078@gmail.com</a></p>

</body>
</html>
