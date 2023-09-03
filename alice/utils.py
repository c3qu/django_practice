def create_html_table(columns, data):
    if len(data) == 0:
        return ""
    table = "<table>{}{}</table>"
    table_header = ""
    table_body = ""
    for column in columns.values():
        table_header += "<th>" + column + "</th>"
    table_header = "<tr>" + table_header + "</tr>"

    for row in data:
        table_row = ""
        for key in columns:
            table_row += "<td>" + str(row.get(key, "")) + "</td>"
        table_body += "<tr>" + table_row + "</tr>"

    print(table.format(table_header, table_body))


if __name__ == '__main__':
    create_html_table({"name": "姓名", "age": "年龄"}, [])
