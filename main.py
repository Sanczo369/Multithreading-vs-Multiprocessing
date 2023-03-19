import os
import platform
import sys

# funkcja sumujaca
def sumFunction(number):
    sum = 0
    for i in range(0, int(number)):
        sum += i


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
            <td>#</td>
            <td>#</td>
            <td>#</td>
            <td>#</td>
          </tr>

          <tr>
            <td>2</td>
            <td>#</td>
            <td>#</td>
            <td>#</td>
            <td>#</td>
          </tr>

          <tr>
            <td>3</td>
            <td>#</td>
            <td>#</td>
            <td>#</td>
            <td>#</td>
          </tr>

          <tr>
            <td>4</td>
            <td>#</td>
            <td>#</td>
            <td>#</td>
            <td>#</td>
          </tr>

          <tr>
            <td>5</td>
            <td>#</td>
            <td>#</td>
            <td>#</td>
            <td>#</td>
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
            <td>#</td>
            <td>#</td>
            <td>#</td>
            <td>#</td>
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