def main():
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Multithreading/Multiprocessing benchmark results</title>
    <style>

    body {
      font-size: 10pt;
    }

    h2 {
      padding-top: 10pt;
    }

    table {
      font-family: arial, sans-serif;
      border-collapse: collapse;
      width: 100%;
      table-layout: fixed ;
    }

    td, th {
      border: 2px solid #b9b9b9;
      padding: 10px;
      text-align: center;
      width: 25% ;
    }

    th {
      background-color: #d5d5d5;
    }

    td {
    }

    tr:nth-child(odd) {
      background-color: #eeeeee;
    }
    </style>
    </head>
    <body>

    <h1>Multithreading/Multiprocessing benchmark results</h1>
    <p>
    </p>

    <h2>Execution environment</h2>
    <p>

    Python version: WERSJA_PYTHONA_DO_PODSTAWIENIA<br/>
    Interpreter: INTERPRETER_DO_PODSTAWIENIA<br/>
    Interpreter version: WERSJA_INTERPRETERA_DO_PODSTAWIENIA<br/>
    Operating system: SYSTEM_OPERACYJNY_DO_PODSTAWIENIA<br/>
    Operating system version: WERSJA_SYSTEMU_DO_PODSTAWIENIA<br/>
    Processor: PROCESOR_DO_PODSTAWIENIA<br/>
    CPUs: LICZBA_CPU_DO_PODSTAWIENIA

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
        <td>TABLICA_1W_1</td>
        <td>TABLICA_4W_1</td>
        <td>TABLICA_4P_1</td>
        <td>TABLICA_max_p_1</td>
      </tr>

      <tr>
        <td>2</td>
        <td>TABLICA_1W_2</td>
        <td>TABLICA_4W_2</td>
        <td>TABLICA_4P_2</td>
        <td>TABLICA_max_p_2</td>
      </tr>

      <tr>
        <td>3</td>
        <td>TABLICA_1W_3</td>
        <td>TABLICA_4W_3</td>
        <td>TABLICA_4P_3</td>
        <td>TABLICA_max_p_3</td>
      </tr>

      <tr>
        <td>4</td>
        <td>TABLICA_1W_4</td>
        <td>TABLICA_4W_4</td>
        <td>TABLICA_4P_4</td>
        <td>TABLICA_max_p_4</td>
      </tr>

      <tr>
        <td>5</td>
        <td>TABLICA_1W_5</td>
        <td>TABLICA_4W_5</td>
        <td>TABLICA_4P_5</td>
        <td>TABLICA_max_p_5</td>
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
        <td>AVG_W1</td>
        <td>AVG_W4</td>
        <td>AVG_P4</td>
        <td>AVG_max_p</td>
      </tr>

    </table>

    <p>App author: Arkadiusz Sanecki</p>

    </body>
    </html>
    '''

if __name__ == '__main__':
    main()