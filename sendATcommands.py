#!/usr/bin/python

import sys, getopt,serial


ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )
ser.open()


def main(argv):
   command = ''
   try:
      opts, args = getopt.getopt(argv,"hc:",["cmd="])
   except getopt.GetoptError:
      print 'python sendATcommands.py -c <command>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'python sendATcommands.py -c <command>'
         sys.exit()
      elif opt in ("-c", "--cmd"):
	command = arg
	ser.write(command)
   print 'Command->',command

if __name__ == "__main__":
   main(sys.argv[1:])
