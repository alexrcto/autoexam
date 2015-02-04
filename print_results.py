import json
import argparse


def print_results(data):
	print("Exam\tFinal")
	print("-" * 13)

	for i, d in sorted(data['grades'].items(), key=lambda x: x[0]):
		exam = i.rjust(4)
		final = ("%.2f" % d['total_grade']).rjust(8)
		print exam, final


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('results', help="The `results.json` file generated by evaluator.py")
	args = parser.parse_args()

	with open(args.results) as fp:
		print_results(json.load(fp))


if __name__ == '__main__':
	main()
