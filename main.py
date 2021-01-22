from expressions import HOME, X_circular_name, X_circular_link
from lxml import html
import requests
import webbrowser


def parser():
	circulares_dict = {}

	try:
		request = requests.get(HOME)

	
	except:

		print(f'ERROR {request.status_code}')

	
	home_html = request.content.decode('utf-8')
	parse = html.fromstring(home_html)
	circular_names = parse.xpath(X_circular_name)
	circular_links = parse.xpath(X_circular_link)

	for i in range(len(circular_names)): #Notice that circular_names and circular_links have the same lenght
		circulares_dict[f'{circular_names[i]}\n'] = HOME + circular_links[i]

	return circulares_dict


def get_new_circulares(dictionary):

	with open('circulares.txt', 'r') as f:

		current_circulares = [line for line in f.readlines()]

	with open('circulares.txt', 'a') as f:

		new_circulares = [k for k in dictionary.keys() if k not in current_circulares]

		for circular in new_circulares:
			f.write(circular)

	return new_circulares


def main():

	circulares_dict = parser()
	new_circulares = get_new_circulares(circulares_dict)

	if len(new_circulares) > 0:
		
		print(f'There\'s {len(new_circulares)} new circulares!\nDo you want to see them? [Y/N]')

		for i in new_circulares:
			print(i)

		user_input = input()

		if user_input.upper() == 'Y':

			for i in new_circulares:

				webbrowser.open(circulares_dict[i])
		else:

			print('OK')


	else:

		print('Ther\'s not new circulares!')


if __name__ == '__main__':

	main()
