import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
status = 'raw'

def analyze_log(log, caseDetection):
	characters = len(log)
	words = len(re.findall(r'\b\w+\b', log))
	numericals = len(re.findall(r'[0-9]', log))
	
	result = {
		'Characters': characters,
		'Words': words,
		'Numeric Digits': numericals,
	}

	if caseDetection == 'y':
		lowercase_count = len(re.findall(r'[a-z]', log))
		uppercase_count = len(re.findall(r'[A-Z]', log))
		total_letters = len(re.findall(r'[a-zA-Z]', log))

		if lowercase_count == total_letters:
			result['Case'] = 'lowercase'
		elif uppercase_count == total_letters:
			result['Case'] = 'uppercase'
		else:
			result['Case'] = 'mixed'
	
	status = 'processed'
	logger.info(f'the log:\t{log}\t is now {status}')
	return result


def clean_and_analyze(log, convert_case='none'):
	if convert_case == 'lower':
		return analyze_log(log.lower(), 'y')
	if convert_case == 'upper':
		return analyze_log(log.upper(), 'y')
	if convert_case == 'none':
		return analyze_log(log)
	
# helper function to clean up printing process
def print_analysis(label, data):
	print(f"{label}\n")
	for key, value in data.items():
		print(f"{str(key)}:\t{value}")
	print('\n')


# start gathering user inputs
string = input('Input a log string: ')
check_case = input('Would you like to detect the case of your log input? (y/n) ')
conversion_type = input('Would you like to make the log (upper) or (lower) case? ')

print_analysis('Analysis Report:', analyze_log(string, check_case))
print_analysis(f'Modified ({conversion_type}) Analysis:', clean_and_analyze(string, conversion_type))