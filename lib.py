import os


def add_invoice(amount):
  cmd = f'lncli addinvoice --amt={amount}'
  os.system(cmd)

def pay_invoice(amount):
  cmd = f'lncli payinvoice --amt={amount}'
  os.system(cmd)


