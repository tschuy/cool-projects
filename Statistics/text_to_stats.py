#!/usr/bin/env python2

from collections import Counter
import pygal
import wordcloud
from os import path
import sys
import argparse

def generateBarChart(text, bar_chart_title):
	word_frequency = []
	top_words = []
	word_list = text.split()
	num_words = len(word_list)
	counted_counter = Counter(word_list)	
	counted_list = counted_counter.most_common(len(counted_counter))

	bar_chart = pygal.HorizontalBar(height=1000)
	bar_chart.title = bar_chart_title
	for i in range(100):
		top_words.append(counted_list[i][0])
		word_frequency.append(100 * counted_list[i][1] / float(num_words))
	bar_chart.x_labels = top_words
	bar_chart.add('', word_frequency)

	bar_chart.render_to_file("top_words.svg")

def generateCloud(text):
	dir = path.dirname(__file__)
	words = wordcloud.process_text(text, max_features=1000)
	elements = wordcloud.fit_words(words, width=1000, height=1000)
	wordcloud.draw(elements, path.join(dir, 'wordcloud.png'), width=1000, height=1000)

def openFile(filename):
	contents = ""
	f = open(filename, 'r')
	for line in f:
		contents = contents + line
	return contents

def parse():
	parser = argparse.ArgumentParser(description='Generate wordcloud and bar charts from text file.')
	parser.add_argument('--file', required=True,
	                   help='Text file containing words to be clouded/charted')
	parser.add_argument('-a', '--chart', action="store_true",
	                   help='Generated bar chart')
	parser.add_argument('-l', '--cloud', action="store_true",
	                   help='Generate word cloud')
	parser.add_argument('-b', '--both', action="store_true",
	                   help='Generate both bar chart and word cloud')

	return parser.parse_args()


def main():
	args = parse()

	text = openFile(args.file)	
	print("File opened.")
	if(args.chart or args.both or (not args.chart and not args.cloud)):
		generateBarChart(text, "Chart from " + args.file)
		print("Bar chart generated.")
	if(args.cloud or args.both or (not args.chart and not args.cloud)):
		generateCloud(text)
		print("Word cloud generated.")

main()
