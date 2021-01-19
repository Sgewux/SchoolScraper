from lxml import html
import requests
import webbrowser

HOME = 'https://www.colegiocomfenalcoibague.edu.co/'

X_circular_name = '//div[@class ="gkTabsItem gk-opacity gk-active"]/div/table/tbody/tr/td/a/text()'

X_circular_link = '//div[@class ="gkTabsItem gk-opacity gk-active"]/div/table/tbody/tr/td/a/@href'


def parser():
	circulares_dict = {}

	try:
		request = requests.get(HOME)

		if request.status_code == 200:
			home_html = request.content.decode('utf-8')
			parse = html.fromstring(home_html)
			circular_names = parse.xpath(X_circular_name)
			circular_links = parse.xpath(X_circular_link)

			for i in range(len(circular_names)): #Notice that circular_names and circular_links have the same lenght
				circulares_dict[f'{circular_names[i]}\n'] = HOME + circular_links[i]

			return circulares_dict



		else:

			raise ValueError

	except ValueError:

		print(f'ERROR {request.status_code}')


def get_new_circulares(dictionary):
	new_circulares = []
	current_circulares = []
	with open('circulares.txt', 'r') as f:

		for line in f.readlines():
			current_circulares.append(line)

	with open('circulares.txt', 'a') as f:

		for k in dictionary.keys():

			if k not in current_circulares:

				f.write(k)
				new_circulares.append(k)



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