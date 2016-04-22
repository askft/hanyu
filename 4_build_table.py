
import sys

from dictionary import *


def convert_to_html_table(d, style='', div_class=''):
    s = ''
    for category in d.get_categories():
        s += '<div class="%s">\n' % div_class
#        s += ('  <table cellspacing="0">\n' +
#              '    <tr><th>')
        s += '<h2 align=center>' + category + '</h2>'
#        s += '</th></tr>\n'
        s += '<table cellspacing=0>\n'
        for word in d.get_words_for_category(category):
            s += '    <tr>\n'
            for w in word.list:
                s += '      <td>' + ', '.join(w) + '</td>\n'
            s += '    </tr>\n'
        s += '  </table>\n'
        s += '</div>\n\n'
    return (
        '<html>\n'
        '<head>\n'
        '  <meta charset="utf-8" />\n'
        '  <style>\n'
        + style +
        '  </style>\n'
        '</head>\n'
        '<body>\n'
        + s +
        '</body>\n'
        '</html>\n'
    )


def main(input, output):
    with open(input, 'r', encoding='utf-8') as file:
        d = create_dictionary_from_file(file)

    style = """
        div {
            max-width: 800px;
            background: #fafafa;
            padding: 1em;
            margin-bottom: 1em;
            border: thin solid #ccc;
        }

        table {
            width: 100%;
            table-layout: fixed;
        }

        table td {
            padding: 0.5em;
        }

        table tr:nth-child(odd) {
            background: #eee;
        }
    """

    html = convert_to_html_table(d, style=style)

    with open(output, 'w', encoding='utf-8') as out:
        out.write(html)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: python %s <input file> <output file>" % sys.argv[0])
        exit(1)
    main(sys.argv[1], sys.argv[2])
