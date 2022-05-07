import os
import subprocess
import json


def add_invoice(amount):
  result = subprocess.run(['lncli', 'addinvoice', f'--amt={amount}'], stdout=subprocess.PIPE)
  dict_str = result.stdout
  d = json.loads(dict_str)
  return d['payment_request']


def pay_invoice(invoice_str):
  '''
  Takes an output from `add_invoice()`
  '''
  result = subprocess.run(['lncli', 'payinvoice', '--json', invoice_str], stdout=subprocess.PIPE)
  dict_str = result.stdout
  d = json.loads(dict_str)
  return d  


def decodepayreq(invoice_str):
  '''
  Takes an output from `add_invoice()`
  '''
  result = subprocess.run(['lncli', 'decodepayreq', invoice_str], stdout=subprocess.PIPE)
  dict_str = result.stdout
  d = json.loads(dict_str)
  return d
