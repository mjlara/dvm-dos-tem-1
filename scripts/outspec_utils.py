#!/usr/bin/env python

# Tobey Carman April 2018
# Utility script for handling dvmdostem output_spec files.
# The output_spec files are expected to be a csv file with 
# a header row and the following fields:

# Name, Description, Units, Yearly, Monthly, Daily, PFT, Compartments, Layers, Placeholder

# An empty field means that variable is not specified (turned on) for output at
# that particular resolution (timestep or PFT or layer, etc).

# A field containing 'invalid' means that the variable is not avaiable or is 
# meaningless at that particular resolution.

# A field containing anything other than "invalid" or an empty string is
# considered to be on or active. While any charachter or string can be used, 
# generally we have been using the first letter of the resolution in 
# question, i.e. 'y' in the field for 'Yearly'.

import csv
import sys
import argparse
import textwrap

def print_line_dict(d, header=False):
  if header:
    print "{:>20s} {:>20s} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}     {:}".format('Name','Units','Yearly','Monthly','Daily','PFT','Compartments','Layers','Description')
  else:
    print "{Name:>20s} {Units:>20s} {Yearly:>12} {Monthly:>12} {Daily:>12} {PFT:>12} {Compartments:>12} {Layers:>12}     {Description}".format(**d)

def list_pft_vars(list_of_lines):
  print_line_dict({}, header=True)
  for i in list_of_lines:
    if i['PFT'] != 'invalid':
      print_line_dict(i)

def list_layer_vars(list_of_lines):
  print_line_dict({},header=True)
  for i in list_of_lines:
    if i['Layers'] != 'invalid':
      print_line_dict(i)

def csv_file_to_data_dict_list(fname):
  
  expected_cols_sorted = ['Compartments', 'Daily', 'Description', 'Layers',
      'Monthly', 'Name', 'PFT', 'Placeholder', 'Units', 'Yearly']

  with open(fname, 'r') as f:
    s = f.readlines()
  
  data = []  
  for r in csv.DictReader(s):
    if sorted(r.keys()) != expected_cols_sorted:
      raise RuntimeError("Bad output spec file!")
    data.append(r)

  return data

def write_data_to_csv(data, fname):
    with open(fname, 'w') as csvfile:
      fieldnames = "Name,Description,Units,Yearly,Monthly,Daily,PFT,Compartments,Layers,Placeholder".split(",")
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(data)

def toggle_off_variable(data, var):
  for line in data:
    if line['Name'] == var:
      for key in "Compartments,Layers,Monthly,Daily,Yearly".split(","):
        if line[key] == 'invalid':
          pass
        else:
          line[key] = ''
          print "Turning {} off for {} resolution".format(var, key)
  return data

def toggle_on_variable(data, var, res_spec):

  for line in data:
    if 'Name' not in line.keys():
      print "ERROR!"
      sys.exit()

    if line['Name'] == var:

      # print "BEFORE"
      # print line
      def safe_set(data_dict, key, new):
        '''Modify dict in place. Pass by name python sementics.'''
        if data_dict[key] == 'invalid':
          print "passing: {} at {} resolution is set to invalid, not setting to '{}'".format(data_dict['Name'], key, new)
        else:
          data_dict[key] = new

      # Work from coarsest to finest so that if the user specifies
      # (for some reason) yearly *and* daily, the daily overwrites
      # the yearly setting.
      if any([r.lower() in ('y','year','yr','yearly') for r in res_spec]):
        safe_set(line, 'Yearly', 'y')
        safe_set(line, 'Monthly', '')
        safe_set(line, 'Daily', '')

      if any([r.lower() in ('m','month','monthly') for r in res_spec]):
        safe_set(line, 'Yearly', 'y')
        safe_set(line, 'Monthly', 'm')
        safe_set(line, 'Daily', '')

      if any([r.lower() in ('d','day','daily',) for r in res_spec]):
        safe_set(line, 'Yearly', 'y')
        safe_set(line, 'Monthly', 'm')
        safe_set(line, 'Daily', 'd')

      # Same for PFTs, work from coarsest to finest
      if any([r.lower() in ('p','pft',) for r in res_spec]):
        safe_set(line, 'PFT', 'p')
        safe_set(line, 'Compartments', '')

      if any([r.lower() in ('c','cpt','compartment','cmpt',) for r in res_spec]):
        safe_set(line, 'PFT', 'p')
        safe_set(line, 'Compartments', 'c')

      # And finally the layers...
      if any([r.lower() in ('l','layer','lay') for r in res_spec]):
        safe_set(line, 'Layers', 'l')


      #from IPython import embed; embed()
      if line['PFT'] == 'invalid' or line['PFT'] == '':
        pass # Who cares..
      else:
        if all([x == 'invalid' or x == '' for x in [line['Yearly'], line['Monthly'], line['Daily']]]):
          print "WARNING! Invalid setting detected! You might not get output for {}".format(line['Name'])

      if line['Compartments'] == 'invalid' or line['Compartments'] == '':
        pass # Who cares..
      else:
        if all([x == 'invalid' or x == '' for x in [line['Yearly'], line['Monthly'], line['Daily']]]):
          print "WARNING! Invalid setting detected! You might not get output for {}".format(line['Name'])

      if line['Layers'] == 'invalid' or line['Layers'] == '':
        pass # Who cares..
      else:
        if all([x == 'invalid' or x == '' for x in [line['Yearly'], line['Monthly'], line['Daily']]]):
          print "WARNING! Invalid setting detected! You might not get output for {}".format(line['Name'])

      # print "AFTER"
      # print line
 
  return data


if __name__ == '__main__':

  '''
  Example API
  ./outputspec_utils.py --list-pft-vars PATH/TO/FILE
  ./outputspec_utils.py --list-layer-vars PATH/TO/FILE
  ./outputspec_utils.py --show-enabled PATH/TO/FILE

  ./outputspec_utils.py --show-enabled PATH/TO/FILE

  ./outspec_utils.py --on LAI yearly PATH/TO/FILE
  ./outspec_utils.py --off LAI

  '''

  parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
      Script for dealing with the output specification csv file.
    ''')
  )
  parser.add_argument('file', 
      #type=argparse.FileType('r'),
      metavar=('FILE'), 
      help=textwrap.dedent('''The file to analyze.'''))

  parser.add_argument('--list-pft-vars', action='store_true',
      help=textwrap.dedent(''''''))

  parser.add_argument('--list-layer-vars', action='store_true',
      help=textwrap.dedent(''''''))

  parser.add_argument('-s','--summary', action='store_true',
      help=textwrap.dedent('''---???---'''))

  parser.add_argument('--on', 
      nargs='+', metavar=('VAR', 'RES',),
      help=textwrap.dedent(''''''))

  parser.add_argument('--off', 
      nargs=1, metavar=('VAR'),
      help=textwrap.dedent(''''''))

  parser.add_argument('--empty', action='store_true',
      help=textwrap.dedent('''---???---'''))

  args = parser.parse_args()
  print args

  if args.list_pft_vars:
    data = csv_file_to_data_dict_list(args.file)
    list_pft_vars(data)

  if args.list_layer_vars:
    data = csv_file_to_data_dict_list(args.file)
    list_layer_vars(data)

  if args.summary:
    data = csv_file_to_data_dict_list(args.file)
    print_line_dict(data[0], header=True)
    for line in data:
      if all([line[x] == 'invalid' or line[x] == '' for x in ['Yearly','Monthly','Daily','PFT','Compartments','Layers']]):
        pass # Nothing turned on...
      else:
        print_line_dict(line)
    sys.exit()

  if args.on:
    if len(args.on) < 2:
      raise ValueError("--on flag requires variable and resolution specification (monthly, pft, layer, etc).")

    var = args.on[0]
    res_spec = args.on[1:]
    data = csv_file_to_data_dict_list(args.file)
    
    data = toggle_on_variable(data, var, res_spec)

    write_data_to_csv(data, "some.csv")

    sys.exit()

  if args.off:
    var = args.off[0].upper()
    data = csv_file_to_data_dict_list(args.file)

    data = toggle_off_variable(data, var)

    write_data_to_csv(data, "some.csv")

    sys.exit()





