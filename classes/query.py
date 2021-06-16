import requests

class Query:
    def __init__(self):
        pass
        
    def send_query(self, query):
        print(f'\nSearching for {query}...')

        # Results list is defined with a length of 5
        results_list = [{},{},{},{},{}]
        output_message = ['Here are your results:',]

        # API call to Google Books using 'requests' package
        response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={query}")
        data = response.json()

        # Append json response data to the results_list
        for i, results in enumerate(results_list):
            try:
                results['title'] = data['items'][i]['volumeInfo']['title']
            except KeyError or IndexError:
                # print("No results available")
                break
            try:
                results['authors'] = data['items'][i]['volumeInfo']['authors'][0]
            except KeyError or IndexError:
                results['authors'] = 'author unknown'
            try:
                results['publisher'] = data['items'][i]['volumeInfo']['publisher']
            except KeyError or IndexError:
                results['publisher'] = 'publisher unknown'

        # Generate concatenated string output message from results_list
        for j in range(len(results_list)):
            try:
                output_message.append(f'\n{j+1}. {results_list[j]["title"]} by {results_list[j]["authors"]}')
            except KeyError or IndexError:
                output_message = ["No results available"]
                break
        listToStr = ' '.join(map(str,output_message))
        output = [listToStr,results_list]
        return output