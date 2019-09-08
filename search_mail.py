#!/usr/bin/python3
# coding: utf-8 

import imaplib
import base64
import email
import sys
import datetime
import email.utils
import time

email_user = 'УЧЕТНАЯ ЗАПИСЬ'
email_pass = 'ПАРОЛЬ ОТ УЧЕТНОЙ ЗАПИСИ'
email_server = 'imap.yandex.ru' # так же работает на gmail.com 
email_port = 993

from_address = '(FROM "info@itbegin.ru")'
subject_head = '(SUBJECT "Help Desk")'
mail = imaplib.IMAP4_SSL(email_server, email_port)
mail.login(email_user, email_pass)

mail.select()           # Подключаемся к почтовому ящику
mail.select('inbox')    # Выбираем папку или метку (в google) из которой хотим считать почту 
# Тестируем 
# mail_one = mail.select("inbox")
# print (mail_one)
 
type, data = mail.search(None, from_address) 
mail_ids = data[0]
id_list = mail_ids.split()

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)')
    raw_email = data[0][1]

for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1].decode('utf-8'))
            #email_subject = msg['subject']
            email_from = msg['from']
            email_time = msg['date']
            convert_in_timestamp = time.mktime(email.utils.parsedate(email_time))
            print ('Date : ' + email_time + '\n')
            print ('Date in_timestamp : ' + '\n')
            print (int(convert_in_timestamp))
            print ('\n')
            print ('From : ' + email_from + '\n')
            #print ('Subject : ' + email_subject + '\n')
