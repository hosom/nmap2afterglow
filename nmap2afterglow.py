# -*- coding: utf-8 -*-

import xml.etree.ElementTree as et
import itertools
import collections

from argparse import ArgumentParser


def parse_args():
	'''
	Parses arguments out and returns them to the main body of the script.
	'''
	desc = 'Converts Nmap XML output to Afterglow friendly input format'
	parser = ArgumentParser(description=desc)
	parser.add_argument('source', type=str,
									help='Source file.')
	parser.add_argument('-o', '--output', type=str,
									help='Destination file.')
									
	return parser.parse_args()

def hops(root):
	'''
	Receives the document root of an Nmap XML file.
	Yields the hops from each host's traceroute.
	'''
	for host in root.iter('host'):
		for trace in host.iter('trace'):
			yield [hop.attrib['ipaddr'] for hop in trace.iter('hop')]

def pairs(hops):
	'''
	Accepts the hops from a host's traceroute in an Nmap XML file.
	Yields pairs indicating paths in a network.
	'''
	hop_iter = iter(hops)
	window = collections.deque(itertools.islice(hop_iter, 1), maxlen=2)
	
	for hop in hops:
		window.append(hop)
		yield tuple(window)
			
def main():

		# Process arguments into useful information.
		args = parse_args()
		file = args.source
		
		# Open the Nmap XML file into an xml parsing tree.
		tree = et.parse(file)
		root = tree.getroot()
		
		# Get routes obtained from the Nmap scan.
		routes = [hop for hop in hops(root)]
		
		# Massage those routes into pairs indicating paths.
		lines = []
		for route in routes:
			for pair in pairs(route):
				lines.append(','.join(pair))
				
		# If an output file was specified, write to the file.
		if args.output:
			with open(args.output, 'wb') as f:
				for line in lines:
					f.write(line + '\n')
		# Otherwise, write to STDOUT
		else:
			for line in lines:
				print line
	
if __name__ == '__main__':
	main()