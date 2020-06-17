import json
import re

html_tags = re.compile(r'<[^>*]+>')
wordpress_tags = re.compile(r'\[[^()]*\]')
round_brackets = re.compile(r'\([^()]*\)')

def remove_html_tags(text):
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    return html_tags.sub('', text)
    
def remove_wordpress_tags(text):
    return wordpress_tags.sub('', text)

def remove_functions(text):
    return round_brackets.sub('', text)

def clean_the_content(text):
    text = remove_html_tags(text)
    text = remove_wordpress_tags(text)
    text = text.lower().strip()
    
    text = re.sub(r'[^a-z0-9\s]', '', text)
    for i in range(1,10):
        text = remove_functions(text)

    # text = text.lower().strip()

    return text

# my_text = "<!-- wp:paragraph -->\n<p>You are breaking the law if you help, suggest or encourage a public servant to commit the crimes of accepting money or gifts in addition to their salary or property from business associates, even if the crime was not successfully committed. You can be sent to jail for a period of 3 to 7 years and will also have to pay a fine.</p>\n<!-- /wp:paragraph -->\n\n<!-- wp:paragraph -->\n<p><strong>Example</strong>: Rajesh, Ravi's cousin offers Mukesh (a public servant) a new house in return for appointing Ravi to the post of junior Railway officer. Even if Ravi does not get the post, Rajesh has \\u201cabetted\\u201d or helped Mukesh break the law.</p>\n<!-- /wp:paragraph -->"
# ans = remove_tags(my_text)
# print(ans)

def DataPrepare():

    my_dict = {'slug': '', 'question': '', 'answer': ''}

    my_list = []

    with open("./JSONData/myData.json") as json_file:
        json_data = json.load(json_file)
        
        for data in json_data:
            my_data = data['rss']['channel']['item']
            # print(my_data)

            for item in my_data:
                my_dict = {'question': '', 'answer': ''}
                
                my_dict['question'] = clean_the_content(str("what is ")+item['title'])



                answer = item['content:encoded']
                answer = clean_the_content(answer)

                my_dict['answer'] = answer

                my_list.append(my_dict)
            
                # print(my_list)
        
    with open('my_data.json', 'a+') as output_file:

        json.dump(my_list, output_file)

    print(len(my_list))


if __name__ == '__main__':
    DataPrepare()