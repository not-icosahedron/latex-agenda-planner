from calendar import monthrange
from datetime import date


def get_month(id):
    spanish = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
              9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
    english = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
              9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    #return spanish[id]+" - "+english[id]
    return spanish[id]

def get_weekday(id):
    spanish = {0: 'Lunes', 1:'Martes', 2:'Mi\\\'ercoles', 3:'Jueves', 4:'Viernes', 5:'S\\\'abado', 6:'Domingo'}
    return spanish[id]

def create_calendar(year, month):
    var = "\\pagestyle{empty} % Removes the page number from the bottom of the page \n" \
          "\\noindent \n" \
          "\\StartingDayNumber=2 % Calendar starting day, default of 1 means Sunday, 2 for Monday, etc \n%---------------------------------------------------------------------------------------- \n" \
          "%	MONTH AND YEAR SECTION \n" \
          "%---------------------------------------------------------------------------------------- \n" \
          "\\begin{center} \n" \
          "\\textsc{\\Huge \color{RawSienna}" + get_month(month) + "}\\\\ % Month \n" \
                                                   "\\textsc{\\large " + str(year) + "} % Year \n" \
                                                                                     "\\end{center} \n" \
                                                                                     "%---------------------------------------------------------------------------------------- \n" \
                                                                                     "\\begin{calendar}{13.8cm} \n"
    begin, days = monthrange(year, month)
    for i in range(begin):
        var += "\\BlankDay \n"
    var += "%---------------------------------------------------------------------------------------- \n" \
           "%	NUMBERED DAYS AND CALENDAR CONTENT \n" \
           "%---------------------------------------------------------------------------------------- \n\n" \
           "% These are the numbered days in the template - if there are less than 31 days simply comment out the bottom lines. \n\n" \
           "% \\vspace{2.5cm} is only there to provide an even look to the calendar where each day is 2.5cm tall, it can be changed or removed to automatically adjust to the day in the week with the most content \n\n" \
           "\\setcounter{calendardate}{1} % Start the date counter at 1 \n\n"
    for j in range(days):
        var += "\\day{}{\\vspace{1.5cm}} % " + str(j + 1) + " \n"
    var += "% Un-comment the \\BlankDay below if the bottom line of the calendar is missing \n" \
           "%\\BlankDay \n\n" \
           "%---------------------------------------------------------------------------------------- \n\n" \
           "\\finishCalendar \n" \
           "\\end{calendar} \n"
    return var


def create_planner(year, month):
    id, days = monthrange(year, month)
    page = 1
    var = "{\\Huge "+get_month(month)+"} ~ {\color{RawSienna} "+str(year)+"} \n \\hfill \\break" \
          "\\hrule depth 0.3mm width \hsize \kern 1pt \hrule width \hsize height 0.2mm \n"
    for day in range(1,days+1):
        if page % 2 != 0:
            var += "\\hfill \\break \\hfill \\break \n{\\Large "+get_weekday(date(year,month,day).weekday())+"} {\\LARGE\color{RawSienna} \\textbf{"+str(day)+"}}  \\hfill \\break" \
            "\hrule width \hsize \kern 2pt" \
            "\\hfill \\break \\hfill \\break \\hfill \\break \\hfill \\break \\hfill \\break \\hfill \\break \n"
        if page % 2 == 0:
            var += "\\hfill \\break \n \\begin{flushright}{\\Large "+get_weekday(date(year,month,day).weekday())+"} {\\LARGE\color{RawSienna} \\textbf{"+str(day)+"}}\\end{flushright}" \
            "\\hrule width \hsize \kern 2pt" \
            "\\hfill \\break \\hfill \\break \\hfill \\break \\hfill \\break \\hfill \\break\n"
        if(day %4 == 0):
            page += 1
            if page % 2 != 0:
                var += "\\newpage {\\Huge "+get_month(month)+"} ~ {\color{RawSienna} "+str(year)+"} \n \\hfill \\break" \
                "\\hrule depth 0.3mm width \hsize \kern 1pt \hrule width \hsize height 0.2mm \n"
            if page % 2 == 0:
                var += "\\newpage \\begin{flushright}{\\Huge "+get_month(month)+"} ~ {\color{RawSienna} "+str(year)+"} \\end{flushright} \n" \
                "\\hrule depth 0.3mm width \hsize \kern 1pt \hrule width \hsize height 0.2mm \n"
    if(page % 2 == 0):
        var += "\\afterpage{\\blankpage}"
    return var

def personal_data():
    var = "\\pagestyle{empty} % Removes the page number from the bottom of the page \n" \
          "\\noindent \n" \
          "{\\Huge Datos personales} \\hfill \\break" \
            "\\hrule depth 0.3mm width \hsize \kern 1pt \hrule width \hsize height 0.2mm \\hfill \\break \n " \
            "\\hfill \\break \nNombre: {\color{RawSienna}\\rule{9.3cm}{0.1mm}}" \
            "\\hfill \\break \nTel\\\'efono: {\color{RawSienna}\\rule{9.2cm}{0.1mm}}" \
            "\\hfill \\break \nCelular: {\color{RawSienna}\\rule{9.4cm}{0.1mm}}" \
            "\\hfill \\break \nE-mail: {\color{RawSienna}\\rule{9.5cm}{0.1mm}}" \
            "\\hfill \\break \nCumplea\~nos: {\color{RawSienna}\\rule{8.7cm}{0.1mm}}" \
            "\\hfill \\break \nTipo de sangre: {\color{RawSienna}\\rule{3.5cm}{0.1mm}}  " \
                            "\nC.P.: {\color{RawSienna}\\rule{3.8cm}{0.1mm}}" \
            "\\hfill \\break \nDirecci\\\'on: {\color{RawSienna}\\rule{9.1cm}{0.1mm}}" \
            "\\hfill \\break \nAlergias: {\color{RawSienna}\\rule{9.3cm}{0.1mm}} \\hfill \\break \\hfill \\break" \
            "\\hfill \\break {\\Large En caso de emergencia informar a:} \\hfill \\break" \
            "\\hrule width \hsize \kern 2pt \\hfill \\break \n " \
            "\\hfill \\break \nNombre: {\color{RawSienna}\\rule{9.3cm}{0.1mm}}" \
            "\\hfill \\break \nTel\\\'efono: {\color{RawSienna}\\rule{9.2cm}{0.1mm}} \\hfill \\break" \
            "\\hfill \\break \nNombre: {\color{RawSienna}\\rule{9.3cm}{0.1mm}}" \
            "\\hfill \\break \nTel\\\'efono: {\color{RawSienna}\\rule{9.2cm}{0.1mm}} \\hfill \\break " \
            "\\hfill \\break {\\Large Notas:} \\hfill \\break" \
            "\\hrule width \hsize \kern 2pt \\hfill \\break \n " \
            "\\afterpage{\\blankpage}"
    return var

f = open('agenda.tex', 'w')
f.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n"
        "% Monthly Calendar \n"
        "% LaTeX Template \n"
        "% \n"
        "% This template has been downloaded from: \n"
        "% http://www.latextemplates.com \n"
        "% \n"
        "% Original calendar style author: \n"
        "% Evan Sultanik (http://www.sultanik.com/LaTeX_calendar_style) \n"
        "% \n"
        "% Important note: \n"
        "% This template requires the calendar.sty file to be in the same directory as the \n"
        "% .tex file. The calendar.sty file provides the necessary structure to create the \n"
        "% calendar. \n"
        "% \n"
        "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n"
        " \n"
        "%---------------------------------------------------------------------------------------- \n"
        "%	PACKAGES AND OTHER DOCUMENT CONFIGURATIONS \n"
        "%---------------------------------------------------------------------------------------- \n"
        " \n"
        "\\documentclass[portrait,a5paper]{article} \n"
        " \n"
        "\\usepackage{calendar} % Use the calendar.sty style \n"
        " \n"
        "\\usepackage[portrait,margin=2cm]{geometry} \n"
        "\\usepackage{color} \n"
        "\\usepackage[dvipsnames]{xcolor} \n"
        "\\usepackage{ragged2e} \n"
        "\\usepackage{afterpage} \n"
        "\\newcommand\\blankpage{% \n"
            "\\null \n"
            "\\thispagestyle{empty}% \n"
            "\\addtocounter{page}{-1}% \n"
            "\\newpage} \n"
        "\\begin{document} \n")

year = date.today().year
f.write(personal_data())
for month in range(1, 13):
    f.write("\\newpage \\newgeometry{left=0cm,bottom=0cm,right=0cm,top=2.3in}")
    f.write(create_calendar(year, month))
    f.write("\\newpage \\restoregeometry \\newpage")
    f.write(create_planner(year, month))
f.write("\\end{document} \n")
