import flet as ft

def main(page:ft.Page):

    page.window_width = 350
    page.window_height = 300
    global operand1, operand_value, operator
    operand1 = 0
    operand_value = False
    operator = '+'

    def bt_clicked(e):
        global operand1, operand_value, operator
        data = e.control.data
        if data == 'AC':
            result.value = '0'
        
        if data in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'):
            if result.value == '0' or operand_value:
                result.value = data
                operand_value = False
            else:
                result.value = result.value + data

        if data in ('+', '-', '*', '/', '='):
            
            if data == '+':
                operand_value = True
                operand1 = result.value
                operator = '+'
            
            elif data == '-':
                operand_value = True
                operand1 = result.value
                operator = '-'
            
            elif data == '*':
                operand_value = True
                operand1 = result.value
                operator = '*'
            
            elif data == '/':
                operand_value = True
                operand1 = result.value
                operator = '/'
            
            if data == '=':
                result.value = calculate(operand1, result.value, operator)

        page.update()

    result = ft.Text('0')
    c1 = ft.Container(ft.Column([
        ft.Row([result], alignment='end'),
        ft.Row([ft.ElevatedButton(text='AC', data='AC', on_click=bt_clicked, expand=1), ft.ElevatedButton('+-', expand=1), ft.ElevatedButton('%', expand=1), ft.ElevatedButton('/', expand=1, data='/', on_click=bt_clicked)], alignment='center'),
        ft.Row([ft.ElevatedButton('7', expand=1, data='7', on_click=bt_clicked), ft.ElevatedButton(text='8', on_click=bt_clicked,  data='8', expand=1), ft.ElevatedButton('9', expand=1, data='9', on_click=bt_clicked), ft.ElevatedButton('*', expand=1, data='*', on_click=bt_clicked)], alignment='center'),
        ft.Row([ft.ElevatedButton('4', expand=1, data='4', on_click=bt_clicked), ft.ElevatedButton('5', expand=1, data='5', on_click=bt_clicked), ft.ElevatedButton('6', expand=1, data='6', on_click=bt_clicked), ft.ElevatedButton('-', expand=1, data='-', on_click=bt_clicked)], alignment='center'),
        ft.Row([ft.ElevatedButton('1', expand=1, data='1', on_click=bt_clicked), ft.ElevatedButton('2', expand=1, data='2', on_click=bt_clicked), ft.ElevatedButton('3', expand=1, data='3', on_click=bt_clicked), ft.ElevatedButton('+', expand=1, data='+', on_click=bt_clicked)], alignment='center'),
        ft.Row([ft.ElevatedButton('0', expand=1, data='0', on_click=bt_clicked), ft.ElevatedButton('.', expand=1, data='.', on_click=bt_clicked), ft.ElevatedButton('=', expand=1, data='=', on_click=bt_clicked)])], width=300))

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.on_resize.get_handler()
    page.add(c1)


def calculate(operand1, operand2, operator):
    result = 0
    if operator == '+':
        result = float(operand1) + float(operand2)
        return result
    
    elif operator == '-':
        result = float(operand1) - float(operand2)
        return result
    
    elif operator == '/':
        if operand2 == '0':
            return 'no division by zero'
        else:
            result = float(operand1) / float(operand2)
            return result
    
    elif operator == '*':
        result = float(operand1) * float(operand2)
        return result


ft.app(target=main)