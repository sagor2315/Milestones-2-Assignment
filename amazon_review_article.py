
import openai
import base64
import requests
# from pprint import pprint
openai.api_key = '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'


def heading_two(text):
    code = f'<!-- wp:heading --><h2> {text}</h2><!-- /wp:heading -->'
    return code


def wp_paragrapg(text):
    code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return code

def open_ai_answer(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    output = response.get('choices')[0].get('text')
    return output

file = open('text.txt','r+')
key = file.readlines()
file.close()
new_key = []
for k in key:
    ist_k = k.strip('\n')
    new_key.append(ist_k)


for keys in new_key:

    title = open_ai_answer(f'write a seo friendly unique eye-catchy killer buying guide title about {keys}')
    content_two = f'write a introduction about {keys}'
    content_three = heading_two(open_ai_answer(f'create a unique seo friendly buying guide subtitle about {keys}')).strip().strip('\n').replace('"','')
    content_four = wp_paragrapg(open_ai_answer(f'now write a unique seo friendly buying guide article about {content_three}'))
    content_five = heading_two(open_ai_answer(f'make a unique seo friendly buying instruction subtitle about {keys}')).strip().strip('\n').replace('"','')
    content_six = wp_paragrapg(open_ai_answer(f'now write another unique seo friendly beneficial article about {content_five}'))
    content_seven = heading_two(open_ai_answer(f'create again another unique seo friendly subtitle about {keys}')).strip().strip('\n').replace('"','')
    content_eight = wp_paragrapg(open_ai_answer(f'now write a unique seo friendly buying article about {content_seven}'))
    content_nine = heading_two('Conclusion')
    content_ten = wp_paragrapg(open_ai_answer(f'at last please write a unique seo friendly conclusion about {keys}'))
    answer = open_ai_answer(content_two).strip().strip('\n')
    cont = answer + content_three + content_four + content_five + content_six + content_seven + content_eight + content_nine + content_ten

    data = {
        'title': title.title().replace('Q:', '').strip().strip('"'),
        'content': cont,
        'slug': keys.replace(' ', '-')
    }

    user = 'sagor'
    password = 'g7HH 3XXS 3LDt UOrR 5PmO UmFE'
    token = base64.b64encode(f'{user}:{password}'.encode())
    header = {'Authorization': f'Basic {token.decode("utf-8")}'}

    api_url = 'https://practice.bathingpicks.com/wp-json/wp/v2/posts'
    post = requests.post(api_url, data=data, headers=header)
    print(post)



