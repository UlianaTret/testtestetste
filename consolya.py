###### from termcolor import c
from termcolor2 import c # termcolor2 + colorama
print (c('red').red.on_white.underline)
print (c('yellow').yellow.on_white.underline)
print (c('green').green.on_white.underline)
print (c('blue').cyan.on_white.underline)
print (c('dark blue').blue.on_white.underline)
print (c('purple').magenta.on_white.underline)

#######
from  prettytable import  PrettyTable
from colorama import Fore, Back, Style
table = PrettyTable()
table.field_names = ['colon1', 'colon2', 'colon3']
table.add_row(["user name", 10, Fore.RED + 'red' + Fore.WHITE])
table.add_row(["user1", 4, 'test1'])
table.add_row(["fsgj", 12, 'test6'])
table.add_row(["nbvc", 5, 'test3'])
table.aling = 'r'
table.sortby = 'colon3'
print(table)