import os
import platform
import sys
import timeit
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

# sum function
def sumFunction(number):
    sum = 0
    for i in range(0, int(number)):
        sum += i

# function for 1 thread
def oneThread(number):
    with ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(sumFunction, number)


# function for 4 threads
def fourThread(number):
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(sumFunction, number)


# function for 4 process
def fourProcess(number):
    with ProcessPoolExecutor(max_workers=4) as pool:
        pool.map(sumFunction, number)


# function for max process
def maxProcess(number):
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as pool:
        pool.map(sumFunction, number)

def main():
    number = [15972490, 80247910, 92031257, 75940266,
              97986012, 87599664, 75231321, 11138524,
              68870499, 11872796, 79132533, 40649382,
              63886074, 53146293, 36914087, 62770938]

    # time tables
    tab_1t = []
    tab_4t = []
    tab_4p = []
    tab_max_p = []

    # for 1 thread
    for i in range(0, 5):
        executionTime = timeit.timeit(lambda: oneThread(number), number=1)
        tab_1t.append(executionTime)
    med_1t = sorted(tab_1t)

    # for 4 thread
    for i in range(0, 5):
        executionTime = timeit.timeit(lambda: fourThread(number), number=1)
        tab_4t.append(executionTime)
    med_4t = sorted(tab_4t)

    # for 4 process
    for i in range(0, 5):
        executionTime = timeit.timeit(lambda: fourProcess(number), number=1)
        tab_4p.append(executionTime)
    med_4p = sorted(tab_4p)

    # for max process
    for i in range(0, 5):
        executionTime = timeit.timeit(lambda: maxProcess(number), number=1)
        tab_max_p.append(executionTime)
    med_max_p = sorted(tab_max_p)


    # HTML
    html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <title>Multithreading/Multiprocessing benchmark results</title>
        <style>

        body {{
          font-size: 10pt;
        }}

        h2 {{
          padding-top: 10pt;
        }}

        table {{
          font-family: arial, sans-serif;
          border-collapse: collapse;
          width: 100%;
          table-layout: fixed ;
        }}

        td, th {{
          border: 2px solid #b9b9b9;
          padding: 10px;
          text-align: center;
          width: 25% ;
        }}

        th {{
          background-color: #d5d5d5;
        }}

        td {{
        }}

        tr:nth-child(odd) {{
          background-color: #eeeeee;
        }}
        </style>
        </head>
        <body>

        <h1>Multithreading/Multiprocessing benchmark results</h1>
        <p>
        </p>

        <h2>Execution environment</h2>
        <p>

        Python version: {str(platform.python_version())}<br/>
        Interpreter: {str(platform.python_implementation())}<br/>
        Interpreter version: {str(sys.version)}<br/>
        Operating system: {str(platform.system())}<br/>
        Operating system version: {str(platform.release())}<br/>
        Processor: {str(platform.processor())}<br/>
        CPUs: {str(os.cpu_count())}

        </p>


        <h2>Test results</h2>
        <p>The following table shows detailed test results:</p>
        <table>
          <tr>
            <th>Execution:</th>
            <th>1&nbsp;thread (s)</th>
            <th>4&nbsp;threads (s)</th>
            <th>4&nbsp;processes (s)</th>
            <th>processes based on number of CPUs (s)</th>
          </tr>

          <tr>
            <td>1</td>
            <td>{str(format(tab_1t[0], '.3f'))}</td>
            <td>{str(format(tab_4t[0], '.3f'))}</td>
            <td>{str(format(tab_4p[0], '.3f'))}</td>
            <td>{str(format(tab_max_p[0], '.3f'))}</td>
          </tr>

          <tr>
            <td>2</td>
            <td>{str(format(tab_1t[1], '.3f'))}</td>
            <td>{str(format(tab_4t[1], '.3f'))}</td>
            <td>{str(format(tab_4p[1], '.3f'))}</td>
            <td>{str(format(tab_max_p[1], '.3f'))}</td>
          </tr>

          <tr>
            <td>3</td>
            <td>{str(format(tab_1t[2], '.3f'))}</td>
            <td>{str(format(tab_4t[2], '.3f'))}</td>
            <td>{str(format(tab_4p[2], '.3f'))}</td>
            <td>{str(format(tab_max_p[2], '.3f'))}</td>
          </tr>

          <tr>
            <td>4</td>
            <td>{str(format(tab_1t[3], '.3f'))}</td>
            <td>{str(format(tab_4t[3], '.3f'))}</td>
            <td>{str(format(tab_4p[3], '.3f'))}</td>
            <td>{str(format(tab_max_p[3], '.3f'))}</td>
          </tr>

          <tr>
            <td>5</td>
            <td>{str(format(tab_1t[4], '.3f'))}</td>
            <td>{str(format(tab_4t[4], '.3f'))}</td>
            <td>{str(format(tab_4p[4], '.3f'))}</td>
            <td>{str(format(tab_max_p[4], '.3f'))}</td>
          </tr>

        </table>

        <h2>Summary</h2>
        <p>The following table shows the median of all results:</p>
        <table>
          <tr>
            <th>Execution:</th>
            <th>1&nbsp;thread (s)</th>
            <th>4&nbsp;threads (s)</th>
            <th>4&nbsp;processes (s)</th>
            <th>processes based on number of CPUs (s)</th>
          </tr>

          <tr>
            <td>Median:</td>
            <td>{str(format(med_1t[2], '.3f'))}</td>
            <td>{str(format(med_4t[2], '.3f'))}</td>
            <td>{str(format(med_4p[2], '.3f'))}</td>
            <td>{str(format(med_max_p[2], '.3f'))}</td>
          </tr>

        </table>

        <p>App author: XYZ</p>

        </body>
        </html>
        """
    with open('html_report.html', 'w') as f:
        f.write(html)
if __name__ == '__main__':
    main()