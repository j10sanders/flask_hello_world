{"filter":false,"title":"invoice_calculator.py","tooltip":"/thinkful/projects/unittest/invoice_calculator.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":24,"column":10},"action":"insert","lines":["def divide_pay(amount, staff_hours):","    \"\"\"","    Divide an invoice evenly amongst staff depending on how many hours they","    worked on a project","    \"\"\"","    total_hours = 0","    for person in staff_hours:","        total_hours += staff_hours[person]","","    per_hour = amount / total_hours","","    staff_pay = {}","    for person in staff_hours:","        pay = staff_hours[person] * per_hour","        staff_pay[person] = pay","","    return staff_pay","","def main():","    staff_pay = divide_pay(360.0, {\"Alice\": 3.0, \"Bob\": 3.0, \"Carol\": 6.0})","    for person, pay in staff_pay.items():","        print(\"{} should be paid ${:.2f}\".format(person, pay))","","if __name__ == \"__main__\":","    main()"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":24,"column":10},"end":{"row":24,"column":10},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1449417814137,"hash":"93d888b80f8b9e883c025a67feae8e6c9d2543e1"}